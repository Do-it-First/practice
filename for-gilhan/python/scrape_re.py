import re
from html import unescape

with open('dp.html') as f:
    html = f.read()

for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
    # 도서 URL 추출
    url = re.search(r'<a href="(.*?)">', partial_html).group(1)
    url = 'https://www.hanbit.co.kr' + url

    # 태그를 제거해서 도서의 제목을 추출함
    title = re.sub(r'<.*?>', '', partial_html)
    title = unescape(title)
    print('url:', url)
    print('title:', title)
    print('----')
