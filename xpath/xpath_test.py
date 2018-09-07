#-*- coding:utf-8 -*-

from lxml import etree

def test1():
	wb_data = '''
		<div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
		'''

	html = etree.HTML(wb_data)
	print html
	#result = etree.tostring(html)
	#print result.decode('utf-8')

	#html_data = html.xpath('/html/body/div/ul/li/a/@href')
	#html_data = html.xpath('/html/body/div/ul/li/a[@href="link.html"]/text()')
	#html_data = html.xpath('//li/a/text()')
	#html_data = html.xpath('//li/a/@href')
	#html_data = html.xpath('//li/a[@href="link2.html"]/text()')
	html_data = html.xpath('//li[last()-1]/a/text()')
	print html_data

	for i in html_data:
		print i

def test2():
	html = etree.parse('test.html')
	html_data = html.xpath('/html/body/div/ul/li/a')
	print html_data

	for i in html_data:
		print i.text()

if __name__ == '__main__':
	test1()

