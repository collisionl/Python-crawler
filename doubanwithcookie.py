# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import http.cookiejar
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://accounts.douban.com/login"
postdata = urllib.parse.urlencode({
    "form_email":"13270330776",
    "form_password":"19970317"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)

file = opener.open(req)
data = file.read()
file = open("/users/collision/desktop/test1.html", "wb")
file.write(data)
file.close()

url2 = "https://movie.douban.com/"
data2 = urllib.request.urlopen(url2).read()
fhandle = open("/users/collision/desktop/test2.html", "wb")
fhandle.write(data2)
fhandle.close()

# mymovie:
# https://movie.douban.com/people/148458209/collect

# rate:  
# <span class="rating  
# -t"></span>

# title:
# <em>
# </em>

# pic:
# <img alt="
# " class="">d

''' <div class="item">
            <div class="pic">
                <a title="Посоки" href="https://movie.douban.com/subject/27018299/" class="nbg">
                    <img alt="Посоки" src="https://img3.doubanio.com/view/movie_poster_cover/ipst/public/p2501705250.webp" class="">
                </a>
            </div>
            <div class="info">
                <ul>
                    <li class="title">
                        <a href="https://movie.douban.com/subject/27018299/" class="">
                            <em>方向 / Посоки</em>
                             / Directions / Posoki
                        </a>
                    </li>
                        <li class="intro">2017-05-26(戛纳电影节) / 瓦西尔·巴诺夫 / 伊万·博尔内夫 / 阿森·布拉特奇基 / 斯特凡·德诺利博夫 / 尼古拉·乌鲁莫夫 / 保加利亚 / 德国 / 马其顿 / 史帝芬·柯曼达瑞夫 / 103分钟 / 方向 / 剧情 / 史帝芬·柯曼达瑞夫 Stephan Komandarev / 西米恩·文希斯拉沃夫 Simeon Ventsislavov / 保加利亚语</li>
                    <li>
                                    <span class="rating3-t"></span>
                        <span class="date">2017-10-16</span>
                        
                    </li>
                    <li>
                        <span class="comment">过于松散，不断提及的保加利亚像一个2小时长的抱怨</span>
                        
                    </li>
                </ul>
            </div>
        </div>
'''