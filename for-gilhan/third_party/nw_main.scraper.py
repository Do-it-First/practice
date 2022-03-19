import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict

file_data = OrderedDict()



mon_data = OrderedDict()

week = [
	"mon",
	"tue",
	"wed",
	"thu",
	"fri",
	"sat",
	"sun",
]

contxt_list = [
	"from",
	"title",
	"thumbnail",
	"detail_link",
	"introduction",
	"writer",
	"genre",
	"age"
]

mon_data = OrderedDict()
tue_data = OrderedDict()
wed_data = OrderedDict()
thu_data = OrderedDict()
fri_data = OrderedDict()
sat_data = OrderedDict()
sun_data = OrderedDict()


week_list = [
	mon_data,
	tue_data,
	wed_data,
	thu_data,
	fri_data,
	sat_data,
	sun_data
]

webtoon_list = [
	"Naver",
	"Daum"
]

# file_data["Naver"] = []

# for day in week:
# 	file_data[day] = None

# print('file_data:')
# print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
i = 0

products = []

for j in range(50):
	products.append("j")

# 작품 여러개를 한 요일에 넣기 시작
product_list = []
for product in products:
	i = i + 1
	dict = OrderedDict()
	print('총 로직 수: ', i)

	# 작품 하나에 정보 넣기 시작
	for info in contxt_list:
		dict[info] = i

		print("마지막 정보 1:", info)
		print("마지막 정보 2:", contxt_list[-1])
		print('~'*20)
		if info == contxt_list[-1]:
			# print(i)
			print("dict: ", dict)
			print("dict: ", type(dict))
			a_prod = json.dumps(dict, ensure_ascii=False, indent="\t")
			print("a_prod: ", a_prod)
			print("a_prod: ", type(a_prod))

			json_form = json.loads(a_prod)
			print("json_form: ", json_form)
			print("json_form: ", type(json_form))
			product_list.append(json_form)
			print("product_list: ", product_list)
			print("product_list: ", type(product_list))
			print('-'*30)
			# print(a_prod.json())
mon_data["mon"] = product_list
a_prod = json.dumps(mon_data, ensure_ascii=False, indent="\t")

			# product_list.append(a_prod)
			# print(json.dumps(product_list, ensure_ascii=False, indent="\t"))

		# print(dict)

# print('week_list_data:')
# print(json.dumps(week_list, ensure_ascii=False, indent="\t"))

# mon_data["from"] = "naver"
# mon_data["title"] = "참교육"
# mon_data["thumbnail"] = "https://shared-comic.pstatic.net/thumb/webtoon/758037/thumbnail/thumbnail_IMAG10_a2297504-4912-4c7e-a5a8-524d6fc77103.jpg"
# mon_data["detail_link"] = "/webtoon/list?titleId=758037&weekday=mon"
# mon_data["introduction"] = "안녕하세요 여기는 소개글 자리입니다."
# mon_data["writer"] = "채용택 / 한가람"
# mon_data["genre"] = "스토리, 액션"
# mon_data["age"] = "15"
print(json.dumps(week_list, ensure_ascii=False, indent="\t"))

# print(week_list)


"""
{
	"Naver": [

	]
}
"""


# for day in week:
# 	file_data[day] = []

print(file_data)





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

