from socket import *
import threading
import argparse

lock=threading.Lock()
openNum=0
threads=[]

def portScanner(host,port):
    global openNum
    try:
        s=socket(AF_INET,SOCK_STREAM)
        #尝试连接，连接不成功会抛出错误
        s.connect((host,port))
        #加锁
        lock.acquire()
        #数量加1
        openNum+=1
        print('[+] %d open' %port)
        #解锁并关闭连接
        lock.release()
        s.close()
    except:
        pass

def main():
    p=argparse.ArgumentParser(description='Port scanner')
    #读入命令行参数
    p.add_argument('-H',dest='hosts',type=str)
    args=p.parse_args()
    hostList=args.hosts.split(',')
    #设置超时时间
    setdefaulttimeout(1)
    #循环多个ip地址
    for host in hostList:
        #开始
        print('scanning the host %s ...' %host)
        #循环端口
        for p in range(5000,10000):
            #开线程
            t=threading.Thread(target=portScanner,args=(host,p))
            #加入线程池并启动线程
            threads.append(t)
            t.start()

        #阻塞进程直到所有线程结束
        for t in threads:
            t.join()
        #结束
        print('[*] The host:%s scan is complete!' %host)
        print('[*] A total of %d open port' %openNum)


if __name__=='__main__':
    main()
    
