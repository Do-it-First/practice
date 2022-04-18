#ridi 키워드 정리

from openpyxl import load_workbook, Workbook

xlsx = "ridibooks_webtoon.xlsx"
wb = load_workbook(xlsx)
ws = wb.active
sheet = wb['Sheet']

man = ['연하남주', '나쁜남자', '후회남주', '집착남주', '계략남주', '다정남주', '순정남주', '상큼남주', '능글남주', '유혹남주', '대형견남주', '츤데레남주', '재벌남주', '능력남주', '평범남주', '무심남주', '바람둥이', '소심남주']
woman = ['능력여주', '나쁜여자', '팜므파탈', '무심여주', '철벽여주', '후회여주', '순정여주', '다정여주', '상큼여주', '순진여주', '소심여주', '평범여주', '츤데레여주', '모범생여주']
mood = ['달달함', '진지함', '감동/힐링', '공포', '원작소설有', '완결', '연재', '단편', '드라마화', '애니화', '영화화']
genre = ['로맨스', '로맨스판타지', '판타지/SF', '시대/역사물', '미스터리/스릴러물', '캠퍼스물', '학원물', '드라마/일상물', '코믹물', '액션/무협물', '스포츠물', '현대배경', '동양배경', '서양배경', '이세계', '디스토피아', '해외웹툰', 'GL', '성인웹툰', 'Lady성인', "Men's성인"]
relation = ['삼각로맨스', '환생/회귀', '빙의/영혼체인지', '차원이동/타임슬립', '복수/배신', '성장물', '친구>연인', '사내연애', '인외/초월적존재', '피폐물', '금지된사랑', '결혼/동거', '계약관계', '짝사랑', '첫사랑', '신분차이', '역하렘', '키잡물', '남장/여장물', '남녀성전환', '연예계', '왕족/귀족', '사제지간', '기억상실', '초능력', '퇴마', '엇갈림/오해']

ridi_list = []

for i in range(2, len(sheet['G'])+1):
    for hh in man + woman:
        sheet['G' + str(i)].value = str(sheet['G' + str(i)].value)\
            .replace("," + hh, "")
            # .replace(hh, "delete").replace(",delete", "")

    ridi_list.append(sheet['G' + str(i)].value)
    # print(sheet['G' + str(i)].value)


ridi_k = []
for h in ridi_list:
    aa = h.split(",")
    ridi_k.append(aa)
ridik_s = sum(ridi_k, [])
set_ridik_s = set(ridik_s)
print(set_ridik_s) #리디 키워드들 중복 제거

#txt파일로 저장
with open("ridi_k.txt", "w", encoding='utf-8') as f:
    f.write(str(set_ridik_s))