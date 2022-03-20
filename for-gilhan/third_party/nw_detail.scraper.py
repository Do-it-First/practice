import requests
from bs4 import BeautifulSoup
import json

f = open("/Users/yong-gilhan/Desktop/School/4-1/시종설/github/practice/for-gilhan/detail_link_list_of_naver.json", 'r')
with open('/Users/yong-gilhan/Desktop/School/4-1/시종설/github/practice/for-gilhan/detail_link_list_of_naver.json') as json_file:
    json_data = json.load(json_file)

json_string = json_data["links"]


week = [
	'mon',
	'tue',
	'wed',
	'thu',
	'fri',
	'sat',
	'sun',
]

for link in json_string:
		print(input())
		html = requests.get(link)
		soup = BeautifulSoup(html.text, 'html.parser')

		wrt_nm = soup.find_all('span', class_='wrt_nm')
		title_tag = soup.find_all('span', class_='title')
		print("name: ", wrt_nm[0].text[7:])
		print("title: ", title_tag[0].text)

		p_tag = soup.find_all('p')

		n = 0
		full_contxt = ""
		for contxt in p_tag[0]:
				n = n + 1
				if str(contxt) != '<br/>':
						full_contxt = full_contxt + str(contxt) + "\n"

		full_contxt = full_contxt[0:-1]
		print("indroduction:" + "\n" + full_contxt)
		genre_tag = soup.find_all('span', class_='genre')
		print("genre: ", genre_tag[0].text)
		age_tag = soup.find_all('span', class_='age')
		print("age: ", age_tag[0].text)
