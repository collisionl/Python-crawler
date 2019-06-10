# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import re
# 忽略访问https时证书不受信任问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

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

if __name__ == '__main__':
    # 模拟为浏览器访问
    headers = ('User-Agent','''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko)
                Chrome/60.0.3112.113 Safari/537.36''')
    opener  = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

    # 总页数
    page_sum = 54
    # 用户ID
    user_id = 148458209

    # 按页爬取
    fhandle = open("豆瓣.txt","w")

    for page in range(page_sum):
        urlStr = "https://movie.douban.com/people/" + str(user_id) + "/collect?start="+str(page*15) + \
        "&sort=rate&rating=all&filter=all&mode=grid"
        print("current page: " + str(page + 1) + " of " + str(page_sum))
        crawl(urlStr, page)

    fhandle.close()

