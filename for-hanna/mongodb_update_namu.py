from pymongo import MongoClient
from collections import OrderedDict
import json


#json 파일 불러오기
with open ("namuwiki_data.json", "r", encoding='utf-8') as f:
    data = json.load(f)
# print(data[-1]['title'])
# print(data[-1]['genre'])
# for i in range(len(data)):
    # print(data[i]["title"])

mongo_info = "mongodb+srv://doitfirst:lPmZ7YI9nexn8qa6@cluster-do-it-first.njk1p.mongodb.net/test"

#DB연결
myclient = MongoClient(
    mongo_info
)

#DB접근
db = myclient['wt_info_db']

#app_crawling_navertoon collection 접근
collection = db['app_crawling_navertoon']

#namuwiki_genre 추가
docs = collection.find()

# for doc in docs:
    # print(doc['title'])

for doc in docs:
    for i in range(len(data)):
        if doc['title'] == data[i]["title"]:
            # collection.update_one({"title": doc['title']}, {'$set': {'namu': data[i]['genre']}})
            collection.update_many({"title": doc['title']}, {'$set': {'namu': data[i]['genre']}})
        else:
            continue

myclient.close()

