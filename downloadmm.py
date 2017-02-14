import urllib.request
import os

def open_url(url):
    response=urllib.request.urlopen(url)
    return response.read()

def get_pageNum(url):
    html=open_url(url).decode('utf-8')
    a=html.find('current-comment-page')+23
    b=html.find(']',a)
    return html[a:b]

def get_imgs(url):
    html=open_url(url).decode('utf-8')
    img_addrs=[]
    a=html.find('img src=')
    while a!=-1: 
        b=html.find('.jpg',a,a+255)
        if b!=-1:
            img_addrs.append(html[a+9:b+4])
        else:
            b=a+9
        a=html.find('img src=',b+4)
    return img_addrs
        
            

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename=each.split('/')[-1]
        print('http:'+each+'\n')
        try:
            img=open_url('http:'+each)
        except:
            pass
        with open(filename,'wb') as f:
            f.write(img)

def downloadpic(folder='pics',page=10):
    os.mkdir(folder)
    os.chdir(folder)

    url='http://jiandan.net/pic/'
    page_num=int(get_pageNum(url))

    for each in range(page_num):
        page_num-=each
        page_url=url+'page-'+str(page_num)+'#comments'
        img_addrs=get_imgs(page_url)
        save_imgs(folder,img_addrs)


if __name__=='__main__':
    downloadpic()
        
