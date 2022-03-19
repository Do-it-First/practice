# urllib으로 웹 페이지 추출하기

from urllib.request import urlopen
import sys

f = urlopen('https://comic.naver.com/webtoon/weekday')

"""
print(type(f))

# print(f.read())

print(f.status) # 상태 코드를 추출

print(f.getheader('Content-Type')) # HTTP 헤더의 값을 추출

"""
# HTTP 헤더를 기반으로 인코딩 방식을 추출(명시X의 경우 utf-8을 사용)
encoding = f.info().get_content_charset(failobj="utf-8")

# 인코딩 방식을 표준 오류에 출력
print('encoding:', encoding, file=sys.stderr)

# 추출한 인코딩 방식으로 디코딩
text = f.read().decode(encoding)
# 웹 페이지의 내용을 표준 출력에 출력
print(text)
