# urllib으로 웹 페이지 추출하기

from urllib.request import urlopen
import sys

f = urlopen('https://www.hanbit.co.kr/store/books/full_book_list.html')

"""
print(type(f))

# print(f.read())

print(f.status) # 상태 코드를 추출

print(f.getheader('Content-Type')) # HTTP 헤더의 값을 추출

"""

encoding = f.info().get_content_charset(failobj="utf-8")

print('encoding:', encoding, file=sys.stderr)

text = f.read().decode(encoding)
print(text)
