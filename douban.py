# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import re
# 忽略访问https时证书不受信任问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 模拟为浏览器访问
headers = ('User-Agent','''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko)
		   Chrome/60.0.3112.113 Safari/537.36''')
opener  = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

# 爬取函数
def crawl(url, page):
	# 爬取URL并转为utf-8码
    html1 = urllib.request.urlopen(url).read().decode("utf-8")
    # 电影详情内容的正则表达式
    pat1 = '<div class="item" >.+?</div>.+?</div>'
    # type(result1) = list
    result1 = re.compile(pat1, re.S).findall(html1)

    for i in result1:
    	# 转为str用于正则匹配
        stringToPat = str(i)
        # 需要匹配的四个内容的正则表达式
        titlePattern = '<em>(.+?)</em>'
        ratePattern = '<span class="rating(\d)-t"></span>'
        commentPattern = '<span class="comment">(.+?)</span>'
        timePattern = '<span class="date">(.+?)</span>'
        # 匹配 type = list
        titleResult = re.compile(titlePattern, re.S).findall(stringToPat)
        rateResult = re.compile(ratePattern, re.S).findall(stringToPat)
        commentResult = re.compile(commentPattern, re.S).findall(stringToPat)
        timeResult = re.compile(timePattern, re.S).findall(stringToPat)
        # 通过 爬取页数的次序 和 本页次序 的和得出 总次序
        fhandle.write(str((result1.index(i)+1) + (page*15)) + ":")
        # 输出 标题 评价 日期
        fhandle.write(titleResult[0] + "\t")					# 为何不输出制表符？
        # 如果有rate则输出 否则输出no rate
        if rateResult:
            fhandle.write("评价：" + rateResult[0] + "星" + "\t")
        else:
            fhandle.write("No rate" + "\t")
        fhandle.write("日期：" + timeResult[0] + "\t")
        fhandle.write("\n")
        # 如果有comment则输出 否则输出no comment
        if commentResult:
            fhandle.write(commentResult[0])
        else:
        	fhandle.write("No Comment")
        fhandle.write("\n\n\n")


# 按页爬取
fhandle = open("/users/collision/desktop/豆瓣.txt","w")

for page in range(41):
	urlStr = "https://movie.douban.com/people/148458209/collect?start="+str(page*15) + \
	"&sort=rate&rating=all&filter=all&mode=grid"
	crawl(urlStr, page)

fhandle.close()



'''


mymovie:
https://movie.douban.com/people/148458209/collect
page41

81771810 page79

第一轮匹配
<div class="item" >.+?</div>\n        </div>

第二轮
title 
 <em>(.+?)</em>

rate
<span class="rating(\d)-t"></span>

comment
<span class="comment">(.+?)</span>

time
<span class="date">(.+?)</span>



<div class="item" >
            <div class="pic">
                <a title="攻殻機動隊2 イノセンス" href="https://movie.douban.com/subject/1291566/" class="nbg">
                    <img alt="攻殻機動隊2 イノセンス" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p453466108.webp" class="">
                </a>
            </div>
            <div class="info">
                <ul>
                    <li class="title">
                        <a href="https://movie.douban.com/subject/1291566/" class="">
                            <em>攻壳机动队2：无罪 / 攻殻機動隊2 イノセンス</em>
                             / Ghost in the Shell 2: Innocence
                        </a>
                            <span class="playable">[可播放]</span>
                    </li>
                        <li class="intro">2004-03-06(日本) / 2004-05-20(戛纳电影节) / 田中敦子 / 大塚明夫 / 山寺宏一 / 竹中直人 / 榊原良子 / 大木民夫 / 日本 / 押井守 / 100分钟 / 攻壳机动队2：无罪 / 剧情 / 科幻 / 动画 / 押井守 Mamoru Oshii / 士郎正宗 Masamune Shirow / 日语 / 粤语</li>
                    <li>
                                    <span class="rating3-t"></span>
                        <span class="date">2017-10-29</span>
                        
                    </li>
                    <li>
                        <span class="comment">导演可能要成佛了，对话高深莫测。不知道是表达不清晰还是别人境界太高了。还是不太懂日本人的审美</span>
                        
                    </li>
                </ul>
            </div>
        </div>


总页数
<span class="thispage" data-total-page="36">1</span>
re
<span class="thispage" data-total-page="(.+?)">1</span>


'''

