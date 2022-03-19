import lxml.html

# tree = lxml.html.parse('full_book_list.html')
tree = lxml.html.parse('full_book_list.html')
html = tree.getroot()
print("tree: ", tree)
print(type(html))

print(type(tree))
"""
# html.xpath('//li')
# html.cssselect('li')

# print(html.xpath('//li'))
# print(html.cssselect('li'))

h1 = html.xpath('//h1')[0]
h = html.xpath('//h1')

print("h: ", h)
print("h1: ", h1)

print("h1.tag: ", h1.tag)
print("h1.text: ", h1.text)
print("h1.get('id'): ", h1.get('id'))
print("h1.attrib: ", h1.attrib)
print("h1.getparent(): ", h1.getparent())
# html.cssselect('li')
"""

for a in html.cssselect('a'):
	print(a.get('href'), a.text)