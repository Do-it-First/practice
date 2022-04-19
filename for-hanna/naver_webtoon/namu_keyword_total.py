#나무위키 키워드 정리

from openpyxl import load_workbook, Workbook

xlsx_list = ["webtoon_mon.xlsx", "webtoon_tue.xlsx","webtoon_sun.xlsx","webtoon_wed.xlsx","webtoon_thur.xlsx","webtoon_fri.xlsx","webtoon_sat.xlsx"]
namu_list = []

for xl in xlsx_list:  
    wb = load_workbook(xl)
    ws = wb.active
    sheet = wb['Sheet']
    for nn in range(1, len(sheet["A"]) + 1):
        sheet['B' + str(nn)].value = str(sheet['B' + str(nn)].value)\
            .replace("None", "").replace("[공포]", "공포").replace("\n", "").replace("SF(사이버펑크", "SF").replace(" 스페이스 오페라)", "SF")
        # print(sheet["B" + str(nn)].value)
        namu_list.append(sheet["B" + str(nn)].value)

print(namu_list)

# namu_k = []
# for h in namu_list:
#     aa = h.split(",")
#     namu_k.append(aa)
# namuk_s = sum(namu_k, [])
# set_namuk_s = set(namuk_s)
# print(set_namuk_s) #나무위키 키워드들 중복 제거

# #txt파일로 저장
# with open("namu_k.txt", "w", encoding='utf-8') as f:
#     f.write(str(set_namuk_s))