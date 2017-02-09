from socket import *
import threading
import argparse

lock=threading.Lock()
threads=[]
openNum=0

def portScanner(host,port):
    global openNum
    try:
        s=socket(AF_INET,SOCK_STREAM)
        s.connect((host,port)) 
        lock.acquire()
        openNum+=1
        print('[+] %d is open' %port)
        lock.release()
        s.close()
    except:
        pass

def main():
    p=argparse.ArgumentParser(description='port scanner')
    p.add_argument('-H',dest='hosts',type=str)
    args=p.parse_args()
    hosts=args.hosts.split(',')
    setdefaulttimeout(1)
    for host in hosts:
        print('scanning the host %s' %host)
        for port in range(5000,10000):
            t=threading.Thread(target=portScanner,args=(host,port))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print('[*]The host:%s is completed' %host)
        print('[*]A total of %d open port' %openNum)


if __name__=='__main__':
    main()
    
