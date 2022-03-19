# meta 태그 안에서 인코딩 방식 추출하기
import re
import sys
from tkinter import E
from urllib.request import urlopen

f = urlopen('https://www.hanbit.co.kr/store/books/full_book_list.html')
bytes_content = f.read()

# charset은 HTML의 앞부분에 적혀 있는 경우가 많으므로
# 응답 본문의 앞부분 1024바이트를 ASCII 문자로 디코딩해 둠
# ASCII 범위 이외의 문자는 U+FFFD(REPLACEMENT CHARACTER)로 변환되어 예외가 발생X

scanned_text = bytes_content[:1024].decode('ascii', errors='replace')

# 디코딩한 문자열에서 정규 표현식으로 charset 값을 추출
match = re.search(r'charset=["\']?([\w-]+)', scanned_text)

if match:
	encoding = match.group(1)

else:
	# charset이 명시돼 있지 않으면 UTF-8을 사용
	encoding = 'utf-8'

# 추출한 이코딩을 표준 오류에 출력
print('encoding:', encoding, file=sys.stderr)

# 추출한 인코딩으로 다시 디코딩
text = bytes_content.decode(encoding)
# 응답 본문을 표준 출력에 출력
print(text)
