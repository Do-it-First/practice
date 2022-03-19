import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://comic.naver.com/webtoon/weekday')

html_text = html_text.text

with open('NW.html', 'w') as html_file:
    html_file.write(html_text)

html = html_text

soup = BeautifulSoup(html, 'html.parser')

"""
my_titles = soup.select(
		'content > div.list_area.daily_all > div > div > ul > li > div > a'
    )

print(my_titles)
for title in my_titles:
    ## Tag안의 텍스트
    print(title.text)
    ## Tag의 속성을 가져오기(ex: href속성)
    print(title.get('href'))
"""

# print("html: ", type(html))
# print("soup: ", type(soup))


col_inners = soup.find_all('div', class_='col_inner')

# print(col_inners)
print(type(col_inners))

# for tag in soup.find_all('a'):
# 	print(tag.attrs)




print("col_inners: ", type(col_inners))
i = 0
for col_inner in col_inners:
	# try:
		
		print("col_inner:", type(col_inner))

		print("col_inner.h4: ", col_inner.h4.text) # @요 웹툰
		i = i + 1
		child = col_inner.descendants
		print("type of child: ", type(child))
		# print("child: ", list(child))
		print(i)
		# print(input())


"""
	except AttributeError:
		print("*"*100)
		pass
	print("!"*200)
"""


# for tag in all_webtoons.children:
# 		print("teg len: ", len(tag))
# 		print("type: ", type(tag))
# 		print(tag)
# 		i = i + 1
# 		print(i)
# 		print("!"*200)

# print(type(all_webtoons[0]))

# 썸네일 path
# content > div.list_area.daily_all > div:nth-child(1) > div > ul > li:nth-child(1) > div > a > img