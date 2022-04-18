#리디북스에서 날짜를 가져오려면 동적 크롤링을 이용해야 한다. selenium을 사용하여 크롤링 실행
from selenium import webdriver
from openpyxl import load_workbook, Workbook
from time import sleep

chromedriver = "C:\manna\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)  


# detail_link = '4761000001?_rdt_sid=event_subgroup&_rdt_idx=0'
# driver.get('https://ridibooks.com/books/'+detail_link)

source_link = 'https://ridibooks.com/keyword-finder/comic?set_id=21'
driver.get(source_link)

# day =  driver.find_element_by_xpath('//*[@id="notice_component"]/ul/li/div[1]/ul/li/h5').text #날짜 뽑는 키워드
# fin = driver.find_element_by_xpath('//*[@id="page_detail"]/div[1]/div[1]/section/article[1]/div[1]/div[3]/p[3]/span[2]').text #완결 미완결 분류
m_list = []
w_list = []
mo_list = []
rel_list = []
gen_list = []

man = driver.find_elements_by_xpath('//*[@id="KeywordFinderRenewal"]/div[1]/fieldset[3]/div/div/div[1]/ul/li/label')
woman = driver.find_elements_by_xpath('//*[@id="KeywordFinderRenewal"]/div[1]/fieldset[4]/div/div/div[1]/ul/li/label/span')
mood = driver.find_elements_by_xpath('//*[@id="KeywordFinderRenewal"]/div[1]/fieldset[5]/div/div/div[1]/ul/li/label/span')
relation = driver.find_elements_by_xpath('//*[@id="KeywordFinderRenewal"]/div[1]/fieldset[2]/div/div/div[1]/ul/li/label/span')
genre = driver.find_elements_by_xpath('//*[@id="KeywordFinderRenewal"]/div[1]/fieldset[1]/div/div/div[1]/ul/li/label/span')

for m in man:
    m_list.append(m.text)
    # print(m.text)
for w in woman:
    w_list.append(w.text)
for mo in mood:
    mo_list.append(mo.text)
for re in relation:
    rel_list.append(re.text)
for ge in genre:
    gen_list.append(ge.text)
# print(day, fin)
# print(man)
driver.quit()

print(m_list)
print(w_list)
print(mo_list)
print(rel_list)
print(gen_list)
