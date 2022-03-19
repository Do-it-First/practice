import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://comic.naver.com/webtoon/weekday')

html_text = html_text.text

with open('NW.html', 'w') as html_file:
    html_file.write(html_text)

html = html_text

soup = BeautifulSoup(html, 'html.parser')

print("html: ", type(html))
print("soup: ", type(soup))


all_webtoons = soup.find('div', class_='list_area daily_all')
i = 0
for tag in all_webtoons:
		print("teg len: ", len(tag))
		print("type: ", type(tag))
		print(tag)
		i = i + 1
		print(i)
		print("!"*200)

print(type(all_webtoons[0]))

content > div.list_area.daily_all > div:nth-child(1) > div > ul > li:nth-child(1) > div > a
content > div.list_area.daily_all > div.col.col_selected > div > ul > li:nth-child(1) > div > a > span