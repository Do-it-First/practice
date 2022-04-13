import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font

xlsx_name = "ridibooks_webtoon"

source_url = "https://ridibooks.com/event/23727"

req = requests.get(source_url)
html = req.content
soup = BeautifulSoup(html, 'lxml')
url_list = []
title_thumbnail = {} #썸네일
title_detail_link = {} #상세페이지
title_writer = {} #작가
title_keyword = {} #이 책의 키워드
title_introduction = {} #작품 소개
title_list = []

for href in soup.find("div", class_ = "event_detail_wrapper").find_all('h3'):
    href_f = href.find("a")
    if href_f is not None:
        url_list.append("https://ridibooks.com"+href.find("a")["href"])
    else:
        continue


# url_list_2 =['https://ridibooks.com/books/4761000001?_rdt_sid=event_subgroup&_rdt_idx=0', 'https://ridibooks.com/books/4762000002?_rdt_sid=event_subgroup&_rdt_idx=1', 'https://ridibooks.com/books/1746013635?_rdt_sid=event_subgroup&_rdt_idx=2', 'https://ridibooks.com/books/4851000020?_rdt_sid=event_subgroup&_rdt_idx=3', 'https://ridibooks.com/books/845018129?_rdt_sid=event_subgroup&_rdt_idx=4', 'https://ridibooks.com/books/3498016405?_rdt_sid=event_subgroup&_rdt_idx=5', 'https://ridibooks.com/books/4716000010?_rdt_sid=event_subgroup&_rdt_idx=6', 'https://ridibooks.com/books/297041115?_rdt_sid=event_subgroup&_rdt_idx=7', 'https://ridibooks.com/books/1746017127?_rdt_sid=event_subgroup&_rdt_idx=8', 'https://ridibooks.com/books/4446000746?_rdt_sid=event_subgroup&_rdt_idx=9', 'https://ridibooks.com/books/297033329?_rdt_sid=event_subgroup&_rdt_idx=10', 'https://ridibooks.com/books/4291002348?_rdt_sid=event_subgroup&_rdt_idx=11', 'https://ridibooks.com/books/1746017141?_rdt_sid=event_subgroup&_rdt_idx=12', 'https://ridibooks.com/books/840027437?_rdt_sid=event_subgroup&_rdt_idx=13', 'https://ridibooks.com/books/297033609?_rdt_sid=event_subgroup&_rdt_idx=14', 'https://ridibooks.com/books/4463000009?_rdt_sid=event_subgroup&_rdt_idx=15', 'https://ridibooks.com/books/1561008157?_rdt_sid=event_subgroup&_rdt_idx=16', 'https://ridibooks.com/books/3776000961?_rdt_sid=event_subgroup&_rdt_idx=0', 'https://ridibooks.com/books/4158000302?_rdt_sid=event_subgroup&_rdt_idx=1', 'https://ridibooks.com/books/4291002350?_rdt_sid=event_subgroup&_rdt_idx=2', 'https://ridibooks.com/books/4403000001?_rdt_sid=event_subgroup&_rdt_idx=3', 'https://ridibooks.com/books/4291003087?_rdt_sid=event_subgroup&_rdt_idx=4', 'https://ridibooks.com/books/1716001591?_rdt_sid=event_subgroup&_rdt_idx=5', 'https://ridibooks.com/books/4158000219?_rdt_sid=event_subgroup&_rdt_idx=6', 'https://ridibooks.com/books/3442000767?_rdt_sid=event_subgroup&_rdt_idx=7', 'https://ridibooks.com/books/4132000010?_rdt_sid=event_subgroup&_rdt_idx=8', 'https://ridibooks.com/books/4291003050?_rdt_sid=event_subgroup&_rdt_idx=9', 'https://ridibooks.com/books/1180010828?_rdt_sid=event_subgroup&_rdt_idx=10', 'https://ridibooks.com/books/1019047195?_rdt_sid=event_subgroup&_rdt_idx=11', 'https://ridibooks.com/books/297037300?_rdt_sid=event_subgroup&_rdt_idx=12', 'https://ridibooks.com/books/4291002530?_rdt_sid=event_subgroup&_rdt_idx=13', 'https://ridibooks.com/books/3776000747?_rdt_sid=event_subgroup&_rdt_idx=14', 'https://ridibooks.com/books/1434012037?_rdt_sid=event_subgroup&_rdt_idx=15', 'https://ridibooks.com/books/1180010861?_rdt_sid=event_subgroup&_rdt_idx=16', 'https://ridibooks.com/books/1515013478?_rdt_sid=event_subgroup&_rdt_idx=17', 'https://ridibooks.com/books/845022210?_rdt_sid=event_subgroup&_rdt_idx=18', 'https://ridibooks.com/books/2107043181?_rdt_sid=event_subgroup&_rdt_idx=19', 'https://ridibooks.com/books/1811181598?_rdt_sid=event_subgroup&_rdt_idx=0', 'https://ridibooks.com/books/4116001097?_rdt_sid=event_subgroup&_rdt_idx=1', 'https://ridibooks.com/books/4291002462?_rdt_sid=event_subgroup&_rdt_idx=2', 'https://ridibooks.com/books/1642009499?_rdt_sid=event_subgroup&_rdt_idx=3', 'https://ridibooks.com/books/505026019?_rdt_sid=event_subgroup&_rdt_idx=4', 'https://ridibooks.com/books/4291002614?_rdt_sid=event_subgroup&_rdt_idx=5', 'https://ridibooks.com/books/4291002679?_rdt_sid=event_subgroup&_rdt_idx=6', 'https://ridibooks.com/books/4291002748?_rdt_sid=event_subgroup&_rdt_idx=7', 'https://ridibooks.com/books/4291002691?_rdt_sid=event_subgroup&_rdt_idx=8', 'https://ridibooks.com/books/2066003274?_rdt_sid=event_subgroup&_rdt_idx=9', 'https://ridibooks.com/books/3776000834?_rdt_sid=event_subgroup&_rdt_idx=10', 'https://ridibooks.com/books/4357000090?_rdt_sid=event_subgroup&_rdt_idx=11', 'https://ridibooks.com/books/4641000001?_rdt_sid=event_subgroup&_rdt_idx=12', 'https://ridibooks.com/books/4291001094?_rdt_sid=event_subgroup&_rdt_idx=13', 'https://ridibooks.com/books/2107076031?_rdt_sid=event_subgroup&_rdt_idx=14', 'https://ridibooks.com/books/845017947?_rdt_sid=event_subgroup&_rdt_idx=15', 'https://ridibooks.com/books/1180009767?_rdt_sid=event_subgroup&_rdt_idx=16', 'https://ridibooks.com/books/1811159043?_rdt_sid=event_subgroup&_rdt_idx=17', 'https://ridibooks.com/books/3093000243?_rdt_sid=event_subgroup&_rdt_idx=18', 'https://ridibooks.com/books/1020005714?_rdt_sid=event_subgroup&_rdt_idx=19', 'https://ridibooks.com/books/505019405?_rdt_sid=event_subgroup&_rdt_idx=20', 'https://ridibooks.com/books/2968002137?_rdt_sid=event_subgroup&_rdt_idx=21', 'https://ridibooks.com/books/4876000001?_rdt_sid=event_subgroup&_rdt_idx=22', 'https://ridibooks.com/books/845020146?_rdt_sid=event_subgroup&_rdt_idx=23', 'https://ridibooks.com/books/4801000001?_rdt_sid=event_subgroup&_rdt_idx=0', 'https://ridibooks.com/books/4291002444?_rdt_sid=event_subgroup&_rdt_idx=1', 'https://ridibooks.com/books/1746014731?_rdt_sid=event_subgroup&_rdt_idx=2', 'https://ridibooks.com/books/3776001006?_rdt_sid=event_subgroup&_rdt_idx=3', 'https://ridibooks.com/books/4291003050?_rdt_sid=event_subgroup&_rdt_idx=4', 'https://ridibooks.com/books/2066003427?_rdt_sid=event_subgroup&_rdt_idx=5', 'https://ridibooks.com/books/4851000001?_rdt_sid=event_subgroup&_rdt_idx=6', 'https://ridibooks.com/books/4291001025?_rdt_sid=event_subgroup&_rdt_idx=7', 'https://ridibooks.com/books/3498016129?_rdt_sid=event_subgroup&_rdt_idx=8', 'https://ridibooks.com/books/297040486?_rdt_sid=event_subgroup&_rdt_idx=9', 'https://ridibooks.com/books/297040249?_rdt_sid=event_subgroup&_rdt_idx=10', 'https://ridibooks.com/books/4516000001?_rdt_sid=event_subgroup&_rdt_idx=11', 'https://ridibooks.com/books/1019018217?_rdt_sid=event_subgroup&_rdt_idx=12', 'https://ridibooks.com/books/297035784?_rdt_sid=event_subgroup&_rdt_idx=13', 'https://ridibooks.com/books/1180010822?_rdt_sid=event_subgroup&_rdt_idx=14', 'https://ridibooks.com/books/297034531?_rdt_sid=event_subgroup&_rdt_idx=15', 'https://ridibooks.com/books/297035050?_rdt_sid=event_subgroup&_rdt_idx=16', 'https://ridibooks.com/books/4524000021?_rdt_sid=event_subgroup&_rdt_idx=17', 
# 'https://ridibooks.com/books/1019020077?_rdt_sid=event_subgroup&_rdt_idx=18', 'https://ridibooks.com/books/4291000714?_rdt_sid=event_subgroup&_rdt_idx=0', 'https://ridibooks.com/books/1746014650?_rdt_sid=event_subgroup&_rdt_idx=1', 'https://ridibooks.com/books/1746011985?_rdt_sid=event_subgroup&_rdt_idx=2', 'https://ridibooks.com/books/3776000826?_rdt_sid=event_subgroup&_rdt_idx=3', 'https://ridibooks.com/books/3228037087?_rdt_sid=event_subgroup&_rdt_idx=4', 'https://ridibooks.com/books/4291002361?_rdt_sid=event_subgroup&_rdt_idx=5', 'https://ridibooks.com/books/3097000702?_rdt_sid=event_subgroup&_rdt_idx=6', 'https://ridibooks.com/books/1019019101?_rdt_sid=event_subgroup&_rdt_idx=7', 'https://ridibooks.com/books/945059919?_rdt_sid=event_subgroup&_rdt_idx=8', 'https://ridibooks.com/books/1180010765?_rdt_sid=event_subgroup&_rdt_idx=9', 'https://ridibooks.com/books/845013860?_rdt_sid=event_subgroup&_rdt_idx=10', 'https://ridibooks.com/books/1962072938?_rdt_sid=event_subgroup&_rdt_idx=11', 'https://ridibooks.com/books/1434011238?_rdt_sid=event_subgroup&_rdt_idx=12', 'https://ridibooks.com/books/3442000645?_rdt_sid=event_subgroup&_rdt_idx=13', 'https://ridibooks.com/books/2968001514?_rdt_sid=event_subgroup&_rdt_idx=14', 'https://ridibooks.com/books/4132000002?_rdt_sid=event_subgroup&_rdt_idx=15', 'https://ridibooks.com/books/845021857?_rdt_sid=event_subgroup&_rdt_idx=16', 'https://ridibooks.com/books/1180009680?_rdt_sid=event_subgroup&_rdt_idx=17', 'https://ridibooks.com/books/4178000708?_rdt_sid=event_subgroup&_rdt_idx=18', 'https://ridibooks.com/books/1515021947?_rdt_sid=event_subgroup&_rdt_idx=19', 'https://ridibooks.com/books/845029171?_rdt_sid=event_subgroup&_rdt_idx=20', 'https://ridibooks.com/books/4876000001?_rdt_sid=event_subgroup&_rdt_idx=21', 'https://ridibooks.com/books/4658000001?_rdt_sid=event_subgroup&_rdt_idx=0', 'https://ridibooks.com/books/4343000476?_rdt_sid=event_subgroup&_rdt_idx=1', 'https://ridibooks.com/books/4291001003?_rdt_sid=event_subgroup&_rdt_idx=2', 'https://ridibooks.com/books/4291002302?_rdt_sid=event_subgroup&_rdt_idx=3', 'https://ridibooks.com/books/4291001951?_rdt_sid=event_subgroup&_rdt_idx=4', 'https://ridibooks.com/books/1746016236?_rdt_sid=event_subgroup&_rdt_idx=5', 'https://ridibooks.com/books/4291001694?_rdt_sid=event_subgroup&_rdt_idx=6', 'https://ridibooks.com/books/4576000001?_rdt_sid=event_subgroup&_rdt_idx=7', 'https://ridibooks.com/books/4291000980?_rdt_sid=event_subgroup&_rdt_idx=8', 'https://ridibooks.com/books/1483022755?_rdt_sid=event_subgroup&_rdt_idx=9', 'https://ridibooks.com/books/4291001482?_rdt_sid=event_subgroup&_rdt_idx=10', 'https://ridibooks.com/books/372006508?_rdt_sid=event_subgroup&_rdt_idx=11', 'https://ridibooks.com/books/1811159044?_rdt_sid=event_subgroup&_rdt_idx=12', 'https://ridibooks.com/books/4443000555?_rdt_sid=event_subgroup&_rdt_idx=13', 'https://ridibooks.com/books/3498016484?_rdt_sid=event_subgroup&_rdt_idx=14', 'https://ridibooks.com/books/4291002928?_rdt_sid=event_subgroup&_rdt_idx=0', 'https://ridibooks.com/books/2968002077?_rdt_sid=event_subgroup&_rdt_idx=1', 'https://ridibooks.com/books/4291001529?_rdt_sid=event_subgroup&_rdt_idx=2', 'https://ridibooks.com/books/4291001300?_rdt_sid=event_subgroup&_rdt_idx=3', 'https://ridibooks.com/books/4291001441?_rdt_sid=event_subgroup&_rdt_idx=4', 'https://ridibooks.com/books/3092008445?_rdt_sid=event_subgroup&_rdt_idx=5', 'https://ridibooks.com/books/4158000183?_rdt_sid=event_subgroup&_rdt_idx=6', 'https://ridibooks.com/books/4291001196?_rdt_sid=event_subgroup&_rdt_idx=7', 'https://ridibooks.com/books/4291000006?_rdt_sid=event_subgroup&_rdt_idx=8', 'https://ridibooks.com/books/4291001079?_rdt_sid=event_subgroup&_rdt_idx=9', 'https://ridibooks.com/books/4800000001?_rdt_sid=event_subgroup&_rdt_idx=10', 'https://ridibooks.com/books/4766000001?_rdt_sid=event_subgroup&_rdt_idx=0', 'https://ridibooks.com/books/3240000001?_rdt_sid=event_subgroup&_rdt_idx=1', 'https://ridibooks.com/books/297025106?_rdt_sid=event_subgroup&_rdt_idx=2', 'https://ridibooks.com/books/297034820?_rdt_sid=event_subgroup&_rdt_idx=3', 'https://ridibooks.com/books/505018405?_rdt_sid=event_subgroup&_rdt_idx=4', 'https://ridibooks.com/books/845018539?_rdt_sid=event_subgroup&_rdt_idx=5', 'https://ridibooks.com/books/505018426?_rdt_sid=event_subgroup&_rdt_idx=6', 'https://ridibooks.com/books/2945000001?_rdt_sid=event_subgroup&_rdt_idx=7', 'https://ridibooks.com/books/297031141?_rdt_sid=event_subgroup&_rdt_idx=0', 'https://ridibooks.com/books/2066001458?_rdt_sid=event_subgroup&_rdt_idx=1', 'https://ridibooks.com/books/847001583?_rdt_sid=event_subgroup&_rdt_idx=2', 'https://ridibooks.com/books/847001317?_rdt_sid=event_subgroup&_rdt_idx=3', 'https://ridibooks.com/books/505002929?_rdt_sid=event_subgroup&_rdt_idx=4', 'https://ridibooks.com/books/847001724?_rdt_sid=event_subgroup&_rdt_idx=5', 'https://ridibooks.com/books/505024190?_rdt_sid=event_subgroup&_rdt_idx=6', 'https://ridibooks.com/books/840036819?_rdt_sid=event_subgroup&_rdt_idx=7', 'https://ridibooks.com/books/847001795?_rdt_sid=event_subgroup&_rdt_idx=8', 'https://ridibooks.com/books/1019006014?_rdt_sid=event_subgroup&_rdt_idx=9', 'https://ridibooks.com/books/847001789?_rdt_sid=event_subgroup&_rdt_idx=10', 'https://ridibooks.com/books/505010096?_rdt_sid=event_subgroup&_rdt_idx=11', 'https://ridibooks.com/books/847002146?_rdt_sid=event_subgroup&_rdt_idx=12', 'https://ridibooks.com/books/847002990?_rdt_sid=event_subgroup&_rdt_idx=13', 'https://ridibooks.com/books/847002488?_rdt_sid=event_subgroup&_rdt_idx=14']
for url in url_list:
    req_url = requests.get(url)
    html_url = req_url.content
    soup_url = BeautifulSoup(html_url, 'lxml')
    
    
    title = soup_url.select_one('#page_detail > div.detail_wrap > div.detail_body_wrap > section > article.detail_header.trackable > div.header_info_wrap > div.info_title_wrap > h3')
    image = soup_url.find("div", class_="thumbnail_image")
    ww = soup_url.find("p", class_="metadata_writer")
    introduction = soup_url.find("article", class_="detail_introduce_book")


    if title is not None:
        title = soup_url.select_one('#page_detail > div.detail_wrap > div.detail_body_wrap > section > article.detail_header.trackable > div.header_info_wrap > div.info_title_wrap > h3').text
        title_list.append(title)
       
        #detail_link, 중복 불허
        title_detail_link[title] = url

        #keyword
        keywords = soup_url.select(".keyword")

    else:
        continue

    keyword_list = []
    

    for num in keywords:
        keyword_list.append(num.get_text())
        title_keyword[title] = keyword_list
        keyword_list=[keyword.strip("#") for keyword in keyword_list] 
    
    #thumbnail url
    if image is not None:
        image = soup_url.find("div", class_="thumbnail_image").find("img")["src"]
        thumbnail_url = "http:" + image
        title_thumbnail[title] = thumbnail_url
    
    #작품 소개
    if introduction is not None:
        introduction = soup_url.find("article", class_="detail_introduce_book").find("p").text
        title_introduction[title] = introduction   
    
    #writer
    if ww is not None:
        ww = soup_url.find("p", class_="metadata_writer").find_all("a")
        writer = []
        for w in ww:
            writer.append(w.text)
            title_writer[title] = "/".join(writer)


    
    # else:
        # continue

# 엑셀파일 쓰기
work_book = Workbook()

# 시트 입력
sheet = work_book.active

key_list= list(title_keyword.keys())
value_list = list(title_keyword.values())
thumbnail = list(title_thumbnail.values())
detail_link_list = list(title_detail_link.values())
introduction_list = list(title_introduction.values())
writer_list = list(title_writer.values())
total_value = ""
introduction_value = ""
writer_value = ""

for jj in range(2, len(title_thumbnail)+2):
    sheet['B' + str(jj)] = key_list[jj-2]
    sheet['B' + str(jj)].font = Font(name="나눔고딕", color="000000")
    sheet['C' + str(jj)] = thumbnail[jj-2]
    sheet['C' + str(jj)].font = Font(name="나눔고딕", color="000000")
    sheet['D' + str(jj)].font = Font(name="나눔고딕", color="000000")
    sheet['D' + str(jj)] = detail_link_list[jj-2]
    introduction_value = introduction_list[jj-2]
    sheet['E' + str(jj)] = "".join(introduction_value)
    sheet['E' + str(jj)].font = Font(name="나눔고딕", color="000000")
    writer_value = writer_list[jj-2]
    sheet['F' + str(jj)] = "".join(writer_value)
    sheet['F' + str(jj)].font = Font(name="나눔고딕", color="000000")
    total_value = value_list[jj-2]
    sheet['G' + str(jj)] = ",".join(total_value)
    sheet['G' + str(jj)].font = Font(name = "나눔고딕", color = "000000")

work_book.save(xlsx_name + ".xlsx")


    

