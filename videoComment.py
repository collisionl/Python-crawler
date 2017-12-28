
import urllib.request
import http.cookiejar
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# 添加cookie
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# type(headers) = dict, 构造headers
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0", 
"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", 
"Accept-Encoding":"gb2312, utf-8", 				# Accept-Encoding为gzip, deflate时可能出现乱码问题，因为浏览器会自动解码 改为utf-8正常
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
"Connection":"keep-alive"}

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


# 需要爬取的视频评论等信息
vid = "1472528692"
comid = "6333634483526987951"
url = "https://coral.qq.com/article/"+vid+"/comment?commentid="+comid+"&reqnum=20"

# 开始爬取
data = urllib.request.urlopen(url).read().decode("utf-8")
# 构建pat并一一匹配
idpat = '"id":"(.*?)"'
userpat = '"nick":"(.*?)"'
comtpat = '"content":"(.*?)"'
idlist = re.compile(idpat, re.S).findall(data)
uesrlist = re.compile(userpat, re.S).findall(data)
comtlist = re.compile(comtpat, re.S).findall(data)
for i in range(0, 20):
	print("users name is: "+eval('u"'+uesrlist[i]+'"'))
	print("comment is: "+eval('u"'+comtlist[i]+'"'))
	print("\n")





'''
https://coral.qq.com/article/1472528692/comment?commentid=6333634483526987951&reqnum=20&tag=&callback=jQuery11240007149744790617918_1510152424611&_=1510152424613
'''

