from selenium import webdriver
from openpyxl import load_workbook, Workbook
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from openpyxl import load_workbook, Workbook

def namuwiki_crawl(workbook, file_name, url, sheet):
    chromedriver = "C:\manna\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)

    #웹툰 정보
    webtoon_genre_a = '//*[@id="wd8ZpUELU"]/article/div[4]/div/div/div/div/div/div[6]/div/div/div/div/div/div/div/div/div/div[6]/div[1]/div/div/table/tbody/tr[3]/td[2]/div/a'  
    webtoon_genre_b = '//*[@id="wd8ZpUELU"]/article/div[4]/div/div/div/div/div/div[6]/div/div/div/div/div/div/div/div/div/div[6]/div[1]/div/div[3]/table/tbody/tr[3]/td[2]/div/a'
    webtoon_genre_c = '//*[@id="wd8ZpUELU"]/article/div[4]/div/div/div/div/div/div[6]/div/div/div/div/div/div/div/div/div/div[6]/div[1]/div/div[2]/table/tbody/tr[3]/td[2]/div/a'
    webtoon_check_genre = '//*[@id="wd8ZpUELU"]/article/div[4]/div/div/div/div/div/div[6]/div/div/div/div/div/div/div/div/div/div[6]/div[1]/div/div/table/tbody/tr[3]/td[1]/div/strong/span'

    try:
        text = driver.find_elements_by_xpath(webtoon_genre_a) #ts물, 로맨스, ..
        check_genre = ""
        total_genre = ""
        try:
            check_genre = driver.find_element_by_xpath(webtoon_check_genre).text
            if len(text) > 0:
                if check_genre == "장르":
                    genre_list = []
                    cnt = 0
                    for zz in text:
                        if cnt == 0:
                            cnt += 1
                            total_genre = zz.text
                        else:
                            genre_list.append(zz.text)
                            total_genre = list(total_genre) + genre_list
        except NoSuchElementException:
            pass
    except ValueError:
        text_b = driver.find_elements_by_xpath(webtoon_genre_b)
        total_genre = ""
        genre_b_list = []
        cnt = 0
        for jj in text_b:
            if cnt == 0:
                cnt += 1
                total_genre = jj.text_b   
            else:
                genre_b_list.append(jj.text_b)
                total_genre = list(total_genre) + genre_b_list
                if len(genre_b_list) == 0:
                    text_c = driver.find_elements_by_xpath(webtoon_genre_c)
                    total_genre = ""
                    genre_c_list = []
                    cnt = 0
                    for kk in text_c:
                        if cnt == 0:
                            cnt += 1
                            total_genre = kk.text_c
                        else:
                            genre_c_list.append(kk.text_c)
                            total_genre = list(total_genre) + genre_c_list
            
    except StaleElementReferenceException:
        print("StaleElementReferenceException")
        return total_genre
    print("total_genre : ", total_genre)
    driver.quit()

    sheet['B' + str(cc)] = total_genre
    workbook.save(file_name)
    return total_genre


file_name = "webtoon_mon.xlsx"
workbook = load_workbook(file_name)
sheet = workbook['Sheet']
#print(sheet.max_row)
cc = 1
for i in sheet['B']:
    url = i.value
    namuwiki_crawl(workbook, file_name, url, sheet)
    cc += 1