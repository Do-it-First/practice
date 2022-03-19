import requests

html_text = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Page Title</title>
    </head>
    <body>

    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>

    </body>
    </html>
"""

html_text = requests.get('https://comic.naver.com/webtoon/weekday')

html_text = html_text.text

# html_file = open('html_file.html', 'w')
# html_file.write(html_text)
# html_file.close()

with open('html_file.html', 'w') as html_file:
    html_file.write(html_text)

# with open('html_file.html', 'a') as html_file:
# 		html_file.write(html_text)


print(type(html_text))