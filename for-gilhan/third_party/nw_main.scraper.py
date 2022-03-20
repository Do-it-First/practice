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

info_keys = [
	"weeks",
	"title",
	"thumbnail",
	"detail_link",
	"introduction",
	"writer",
	"genre",
	"age"
]

# data for practice
information = {
		"weeks" : "월",
		"title" : "참교육",
		"thumbnail" : "https://shared-comic.pstatic.net/thumb/webtoon/758037/thumbnail/thumbnail_IMAG10_a2297504-4912-4c7e-a5a8-524d6fc77103.jpg",
		"detail_link" : "/webtoon/list?titleId=758037&weekday=mon",
		"introduction" : "안녕하세요 여기는 소개글 자리입니다.",
		"writer" : "채용택 / 한가람",
		"genre" : "스토리, 액션",
		"age" : "15"
}

# information = {
# 		info_keys[0]: "월",
# 		info_keys[1]: "참교육",
# 		info_keys[2]: "https://shared-comic.pstatic.net/thumb/webtoon/758037/thumbnail/thumbnail_IMAG10_a2297504-4912-4c7e-a5a8-524d6fc77103.jpg",
# 		info_keys[3]: "/webtoon/list?titleId=758037&weekday=mon",
# 		info_keys[4]: "안녕하세요 여기는 소개글 자리입니다.",
# 		info_keys[5]: "채용택 / 한가람",
# 		info_keys[6]: "스토리, 액션",
# 		info_keys[7]: "15"
# }

def save_one_wt(information):
		webtoon = OrderedDict()
		for info in info_keys:
				webtoon[info] = information[info]
		return webtoon # => orderedDict

def save_prod_list():

		prod_list = []
		for prod in range(3):

				saved_prod = save_one_wt(information)
				prod_list.append(saved_prod)
		processed_prod_list = json.dumps(prod_list, ensure_ascii=False, indent="\t")
		print("processed_prod_list:", processed_prod_list)
		# print('='*80)
		return processed_prod_list

def save_naver_wt():
		webtoon = OrderedDict()
		webtoon['Naver'] = json.loads(save_prod_list())
		webtoon = json.dumps(webtoon, ensure_ascii=False, indent="\t")
		return webtoon

print("here: ", save_naver_wt())

# a_prod = json.dumps(dict, ensure_ascii=False, indent="\t")


html = requests.get('https://comic.naver.com/webtoon/weekday')
soup = BeautifulSoup(html.text, 'html.parser')
doc = soup.prettify()

with open('NW.html', 'w') as html_file:
    html_file.write(doc)

col_inners = soup.find_all('div', class_='col_inner')
i = 0
n = 0
d = week[n]

detail_of_nw_list = []

# wt_list = []
for col_inner in col_inners:
		print("child:2", list(col_inner.children)[1]) # @요 웹툰
		day = list(col_inner.children)[1].text
		for k in list(col_inner.children)[3]('a'):
				# wt_info = OrderedDict() # 초기화
				i = i + 1
				if k.get('title') != None:
						title = k.get('title')
						link = 'https://comic.naver.com' + k.get('href')
						detail_of_nw_list.append(link)
						# wt_info['title'] = title
						# wt_info['link'] = link

				else:
						thumbnail = k.img['src']
						# wt_info['thumbnail'] = thumbnail
				# wt_list.append(wt_info)
				# json.dumps(wt_info, ensure_ascii=False, indent="\t")
		print(week[n], ":", i/2, "개")
		# print(wt_info)
		# json.loads(wt_info)
		i = 0
		n = n + 1


# def detail_links_save(filename, link_list):
# 	file = open(f"{filename}.json", 'w')
# 	for link in link_list:
# 		file.write(link)
# 	f.close()


plain = OrderedDict()
links = []

for link in detail_of_nw_list:
	links.append(link)

plain['links'] = links

link_json = json.dumps(plain, ensure_ascii=False, indent="\t")
print(link_json)

file = open("detail_link_list_of_naver.json", 'w')
file.write(link_json)
file.close()