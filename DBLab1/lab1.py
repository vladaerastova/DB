import string
import requests
import lxml.etree as etree

url1 = 'http://www.bigmir.net/'
root = etree.Element("root")

doc = etree.SubElement(root, "data")
tree = etree.HTML(requests.get(url1).text)
url = tree.xpath('/html/body//a//@href')

tree = etree.HTML(requests.get(url1).text)
img = tree.xpath('/html/body//img/@src')
text = tree.xpath('/html/body//a//text()')
url_el = etree.SubElement(doc,"page", url = url1)
count = 2

for i in img:
    etree.SubElement(url_el, "image").text = i
for i in text:
    etree.SubElement(url_el, "text").text = i
for a in url:
    if(string.find(a, 'holder') == -1 and a !="/"  ):
        if(string.find(a,"http:") == -1):
            a= "http:"+a
        if count <= 20:
            tree = etree.HTML(requests.get(a).text)
            img = tree.xpath('/html/body//img/@src')
            text = tree.xpath('/html/body//a//text()')
            url_el = etree.SubElement(doc,"page", url = a)
            for i in img:
                etree.SubElement(url_el, "image").text = i
            for i in text:
                etree.SubElement(url_el, "text").text = i
#                print i
        count = count + 1

tree = etree.tostring(root, pretty_print = True, encoding = 'utf-8', xml_declaration = True)
f = open("1.xml","w")
f.writelines(tree)
f.close()

2####################################################################

tree = etree.parse("1.xml")
count = 0
min = -1
root = tree.getroot()
text = tree.xpath("//page")
mpage = text[0].attrib
for a in text:
    s = a.xpath(".//image/text()")
    for st in s:
        count = count + 1
    if min == -1:
        min = count
    if count < min:
        min = count
        mpage = a.attrib
    count = 0
print mpage, ":", min

3########################################################################

url = "http://www.sokol.ua/smartphones/c282/"
root = etree.Element("root")

tree = etree.HTML(requests.get(url).text)
doc = etree.SubElement(root, "data")
name = tree.xpath('//div[@class="title"]/a/text()')
image = tree.xpath('//img/@data_src')
price = tree.xpath('//span[@class="uah"]/text()' )

for i in range(20):
    node = etree.SubElement(doc, 'product', id = str(i+1))
    etree.SubElement(node, 'name').text = name[i]
    etree.SubElement(node, 'price').text = price[i]
    etree.SubElement(node, 'image').text = image[i]

tree = etree.tostring(root, pretty_print = True, encoding = 'utf-8', xml_declaration = True)
f = open("3.xml","w")
f.writelines(tree)
f.close()

4#####################################################################

data = open('transform.xsl')
xslt_content = data.read()
xslt_root = etree.XML(xslt_content)
dom = etree.parse('3.xml')
transform = etree.XSLT(xslt_root)
result = transform(dom)
f = open('4.html', 'w')
f.write(str(result))
f.close()