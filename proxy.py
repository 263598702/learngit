import urllib.request
import random

url='http://www.whatismyip.com.tw/'
ipList=['221.0.51.41:9999']

proxy_support=urllib.request.ProxyHandler({'http':random.choice(ipList)})
opener=urllib.request.build_opener(proxy_support)

opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]

urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)

print(response.read().decode('utf-8'))
