#-*- coding:utf-8 -*-
import urllib
import urllib2
from lxml import etree

def loadPage(url,filename):
	"""
	   根据url发送请求，获取服务器响应文件
	   url:需要爬取的url地址
	   filename:处理的文件名
	"""
	print "正在下载"+filename
	print url
	#headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59"}
	request = urllib2.Request(url)
	html = urllib2.urlopen(request).read()
	#print html
	#解析HTML文档为HTML DOM模型
	content = etree.HTML(html)
	#print content
	#返回所有匹配成功的列表集合
	link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
	#link_list = content.xpath('//a/@href')
	#print link_list
	for link in link_list:
		fulllink = "http://tieba.baidu.com"+link	
		print fulllink
		loadImage(fulllink)		

#取出每个帖子里的图片链接
def loadImage(link):
	headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
	request = urllib2.Request(link,headers = headers)
	response = urllib2.urlopen(request)
	html = response.read()
	content = etree.HTML(html)
	#返回帖子里的所有图片连接的列表集合
	link_list = content.xpath('//img[@class="BDE_Image"]/@src')
	for link in link_list:
		writeImage(link)

def writeImage(link):
	"""
	   作用:将html内容写入到本地
	   html:服务器相应文件内容
	"""
	#print "正在保存"+filename
	#文件写入
	headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
	request = urllib2.Request(link,headers = headers)
	img = urllib2.urlopen(request).read()
	filename = link[-10:]
	print filename
	with open(filename,"wb") as f:
		f.write(img)
	print "-"*30

def tiebaSpider(url,beginPage,endPage):
	"""
	   作用:贴吧爬虫调度器，负责组合处理每个页面的url
	   url:贴吧url的前部分
	   baginPage:起始页
	   endPage:结束页
	"""
	for page in range(beginPage,endPage+1):
		pn = (page-1)*50
		filename = "第"+str(page)+"页.html"
		fullurl = url+"&pn="+str(pn)
		#print fullurl
		loadPage(fullurl,filename)
		#print html
		#writePage(html,filename)
	print "谢谢使用"

if __name__ == "__main__":
	kw = raw_input("请输入需要爬取的贴吧名:")
	beginPage = int(raw_input("请输入起始页:"))
	endPage = int(raw_input("请输入结束页："))
	
	url = "http://tieba.baidu.com/f?"
	key = urllib.urlencode({"kw":kw})
	fullurl = url+key
	#print fullurl
	tiebaSpider(fullurl,beginPage,endPage)
