from socket import *
import threading
import argparse

threads=[]
openNum=0
lock=threading.Lock()
nums={}

def scanPort(host,port):
    global openNum
    try:
        s=socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] port %d is open' %port)
        lock.release()
        s.close()
    except:
        pass


def main():
    global openNum
    p=argparse.ArgumentParser(description='port scanner')
    p.add_argument('-H',dest='hosts',type=str)
    args=p.parse_args()
    hosts=args.hosts.split(',')
    setdefaulttimeout(1)
    for host in hosts:
        print('[*] host:%s is scanning' %host)
        for p in range(5000,10000):
            t=threading.Thread(target=scanPort,args=(host,p))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
 
        print('[*] The host:%s scan is completed' %host)
        print('[*] A toal of %d port is open' %openNum)
        openNum=0

if __name__=='__main__':
    main()
