import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import json
import time

# start = time.time()

# xlsx_name = "ridibooks_webtoon"

def ridi_url():
    start = time.time()

    
    source_url = "https://ridibooks.com/event/23727"

    req = requests.get(source_url)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    url_list = []
    
    for href in soup.find("div", class_ = "event_detail_wrapper").find_all('h3'):
        href_f = href.find("a")
        if href_f is not None:
            url_list.append("https://ridibooks.com"+href.find("a")["href"])
        else:
            continue
    a = "time : ",time.time() - start
    print(a)
    return url_list

def ridi_info(url_list):
    start = time.time()

    title_thumbnail = {} #썸네일
    title_detail_link = {} #상세페이지
    title_writer = {} #작가
    title_keyword = {} #이 책의 키워드
    title_introduction = {} #작품 소개

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


    key_list= list(title_keyword.keys())
    value_list = list(title_keyword.values())
    thumbnail = list(title_thumbnail.values())
    detail_link_list = list(title_detail_link.values())
    introduction_list = list(title_introduction.values())
    writer_list = list(title_writer.values())
    data_list = []

    for i in range(len(key_list)):
        data = OrderedDict()
        data["platform"] = "ridibooks"
        data["title"] = key_list[i]
        data["thumbnail"] = thumbnail[i]
        data["detail_link"] = detail_link_list[i]
        data["introduction"] = introduction_list[i]
        data["writer"] = writer_list[i]
        data["genre"] = value_list[i]
        data_list.append(data)
    j = json.dumps(data_list, ensure_ascii=False)
    with open('json_ridi_f.json', 'w', encoding='utf-8') as json_ridi_f:
        json_ridi_f.write(j)

    b = "time : ",time.time() - start
    print(b)
    return b


link_ridi = ridi_url()
# print(link_ridi)
ridi = ridi_info(link_ridi)