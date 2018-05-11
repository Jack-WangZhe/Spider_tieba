#-*- encoding=utf-8 -*-

import urllib
import urllib2

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

formdata = {
"start":"40",
"limit":"20"
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url,data = data ,headers = headers)

response = urllib2.urlopen(request)

print response.read()
