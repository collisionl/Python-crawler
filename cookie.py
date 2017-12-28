# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import http.cookiejar

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes"
postdata = urllib.parse.urlencode({
    "username":"weisuen",
    "password":"aA123456"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)

file = opener.open(req)
data = file.read()
file = open("/users/lcy/desktop/test1.html", "wb")
file.write(data)
file.close()

url2 = "http://bbs.chinaunix.net/"
data2 = urllib.request.urlopen(url2).read()
fhandle = open("/users/lcy/desktop/test2.html", "wb")
fhandle.write(data2)
fhandle.close()