#-*- coding:utf-8 -*-
import urllib
import urllib2

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc"

headers = {
"Accept" : "application/json, text/javascript, */*; q=0.01",
"X-Requested-With" : "XMLHttpRequest",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8"
}
key = raw_input("请输入需要翻译的文字:")
formdata = {
"i" : key,
"type" : "AUTO",
"doctype" : "json",
"xmlVersion" : "1.8",
"keyfrom" : "fanyi.web",
"ue" : "UTF-8",
"action" : "FY_BY_CLICKBUTTION",
"typoResult" : "true"
}
data = urllib.urlencode(formdata)
request = urllib2.Request(url,data = data,headers = headers)
print urllib2.urlopen(request).read()
