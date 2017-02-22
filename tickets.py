"""命令行火车票查看器

Usage:
    tickets [-dgktz] <from> <to> <date>

Options:
    -h, --help 查看帮助
    -d         动车
    -g         高铁
    -k         快速
    -t         特快
    -z         直达

Examples:
    tickets 上海 北京 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
import requests
from docopt import docopt
from prettytable import PrettyTable
from colorama import init,Fore
from stations import stations

init()

class TrainsCollection:

    header='车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()

    def __init__(self,available_trains,options):
        self.available_trains=available_trains
        self.options=options 

    def _get_duration(self,raw_train):
        duration=raw_train.get('lishi').replace(':','小时')+'分'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration
    @property
    def trains(self): 
        for raw_train in self.available_trains:
            raw_train=raw_train['queryLeftNewDTO'] 
            train_no=raw_train['station_train_code']
            initial=train_no[0].lower() 
            if not self.options or initial in self.options:
                train=[
                    train_no,
                    '\n'.join([Fore.GREEN+raw_train['from_station_name']+Fore.RESET,
                               Fore.RED+raw_train['to_station_name']+Fore.RESET]),
                    '\n'.join([Fore.GREEN+raw_train['start_time']+Fore.RESET,
                               Fore.RED+raw_train['arrive_time']+Fore.RESET]),
                    self._get_duration(raw_train),
                    raw_train['zy_num'],
                    raw_train['ze_num'],
                    raw_train['rw_num'],
                    raw_train['yw_num'],
                    raw_train['yz_num'],
                    raw_train['wz_num'],
                ] 
                yield train

    def pretty_print(self):
        pt=PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)

def cli():
    arguments=docopt(__doc__)
    from_station=stations.get(arguments['<from>'])
    to_station=stations.get(arguments['<to>'])
    date=arguments['<date>']
    url=('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(
                date, from_station, to_station
           ) 
    options=''.join([key for key, value in arguments.items() if value is True]) 
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    s=requests.Session()
    s.headers.update(headers)
    r=s.get(url,verify=False) 
    available_trains=r.json()['data']  
    TrainsCollection(available_trains,options).pretty_print()

if __name__=='__main__':
    cli()
        
