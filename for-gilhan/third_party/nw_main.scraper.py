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
i = 0
n = 0
d = week[n]
for col_inner in col_inners:
		print("child:2", list(col_inner.children)[1]) # @요 웹툰
		day = list(col_inner.children)[1].text
		for k in list(col_inner.children)[3]('a'):
				i = i + 1
				if k.get('title') != None:
						title = k.get('title')
						link = 'https://comic.naver.com' + k.get('href')
				else:
						thumbnail = k.img['src']
		print(week[n], ":", i/2, "개")
		i = 0
		n = n + 1
		