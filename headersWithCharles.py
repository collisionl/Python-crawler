import urllib.request
import http.cookiejar

url = "http://news.163.com/16/0825/09/BVA8A9U500014SEH.html"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0", 
"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", 
"Accept-Encoding":"utf-8", 				# Accept-Encoding为gzip, deflate时可能出现乱码问题，因为浏览器会自动解码 改为utf-8正常
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
"Connection":"keep-alive"}

cjar = http.cookiejar.CookieJar()

proxy = urllib.request.ProxyHandler({'http':"127.0.0.1:8888"})
# 添加proxy 通过Charles查看headers
opener = urllib.request.build_opener(proxy, urllib.request.HTTPCookieProcessor(cjar))

# 建立空list，为了以指定的格式存储头信息
headall = []
# for循环遍历dit，构造出指定格式的headers信息
for key,value in headers.items():
	item = (key, value)
	headall.append(item)
# 将指定格式的headers信息添加好
opener.addheaders = headall
# 将opener安装为全局
urllib.request.install_opener(opener)

data = urllib.request.urlopen(url).read()
fhandle = open("/users/collision/desktop/news.html","wb")
fhandle.write(data)
fhandle.close()

'''
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive

# 忽略访问https时证书不受信任问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
'''