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


# all_webtoons = soup.find_all('div', class_='list_area daily_all')
# print(type(soup))
# print(type(all_webtoons))
