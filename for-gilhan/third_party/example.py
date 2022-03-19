import requests

r = requests.get('http://hanbit.co.kr/store/books/full_book_list.html')

# basic
print("type(r): ", type(r))
print("r.status_code: ", r.status_code)
print("r.headers ['content-type']: ", r.headers['content-type'])
print("r.encoding: ", r.encoding)
print("r.text: ", type(r.text)) # str 자료형
print("r.content: ", type(r.content)) # bytes 자료형

# requests로 호출
"""
r = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010')
json = r.json()
print(json)
"""

# requests 세션
"""
s = requests.Session()
r = s.get('http://naver.com/')
print(r.json())
print(type(r))
"""

