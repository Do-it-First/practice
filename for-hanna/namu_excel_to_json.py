#나무위키 엑셀 파일들 namuwiki_data.json으로 생성
from openpyxl import load_workbook, Workbook
from collections import OrderedDict
import json


xlsx_list = ["webtoon_mon.xlsx", "webtoon_tue.xlsx", "webtoon_wed.xlsx", "webtoon_thur.xlsx", "webtoon_fri.xlsx", "webtoon_sat.xlsx", "webtoon_sun.xlsx"]
data_list = []

for xl in xlsx_list:
    wb = load_workbook(xl)
    ws = wb.active
    # print(data)
    sheet = wb['Sheet']
    
    for i in range(1, len(sheet["A"])+1):
        data = OrderedDict()
        data["title"] = sheet["A" + str(i)].value
        aa = str(sheet["B" + str(i)].value)\
            .replace("\n", ", ")\
            .replace(",,", ",")
        data["genre"] = aa
        data["day"] = xl[8:11]
        data_list.append(data)
print(data_list)

j = json.dumps(data_list, ensure_ascii=False)

with open('namuwiki_data.json', 'w', encoding='utf-8') as f:
    f.write(j)