#-*- coding:utf-8 -*-

import urllib2

url = "http://www.renren.com/880151247/profile"

headers = {
"Host" : "www.renren.com",
"Connection" : "keep-alive",
"Accept" : "application/json, text/javascript, */*; q=0.01",
"X-Requested-With" : "XMLHttpRequest",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
"Referer" : "http://www.renren.com/965887018",
#"Accept-Encoding" : "gzip, deflate, sdch",
"Accept-Language" : "zh-CN,zh;q=0.8",
"Cookie" : "抓包返回"
}

request = urllib2.Request(url,headers = headers)

response = urllib2.urlopen(request)

print response.read()
