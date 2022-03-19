import requests
from bs4 import BeautifulSoup

week = [
	'mon',
	'tue',
	'wed',
	'thu',
	'fri',
	'sat',
	'sun',
]

html = requests.get('https://comic.naver.com/webtoon/weekday')
soup = BeautifulSoup(html.text, 'html.parser')
doc = soup.prettify()

with open('NW.html', 'w') as html_file:
    html_file.write(doc)

col_inners = soup.find_all('div', class_='col_inner')


print(type(col_inners))

print("col_inners: ", type(col_inners))
i = 0
for col_inner in col_inners:
		print("child:1 ", list(col_inner.children)[0])
		print('!'*100)
		print("child:2", list(col_inner.children)[1]) # @요 웹툰
		print('!'*100)
		print("child:3 ", list(col_inner.children)[2])
		print('!'*100)
		# print("child:4 ", list(col_inner.children)[3]) # ul
		print("child: ", len(list(col_inner.children)[3])) # ul

		for k in list(col_inner.children)[3]('a'):
				if k.get('title') != None:
					print('o'*80)
					print(type(k))
					print("title: ", k.get('title'))
					print("link: ", 'https://comic.naver.com' + k.get('href'))
				else:
					print('!'*80)
					print(type(k))
					print("img: ", k.img['src'])
					print(k)
				print("^^"*30)


		print('!'*100)
		print("child:5 ", list(col_inner.children)[4])
		print('!'*100)
		
		print("col_inner:", type(col_inner))

		print("col_inner.h4: ", col_inner.h4.text) # @요 웹툰
		i = i + 1
		child = col_inner.descendants
		print("type of child: ", type(child)) # generator
		# print("child: ", list(child))
		print(i)
		print(input())
		print('*'*100)

