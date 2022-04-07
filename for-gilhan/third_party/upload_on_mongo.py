import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps, loads
from bson import json_util
import json

# mongo_info = os.environ['mondb_URI']

mongo_info = "mongodb+srv://doitfirst:lPmZ7YI9nexn8qa6@cluster-do-it-first.njk1p.mongodb.net/test"


myclient = pymongo.MongoClient(
    mongo_info
)



mydb = myclient.wt_info_db
print("mydb: ", mydb)
print(type(mydb))
myinform = mydb.inform
print("myinform: ", type(myinform))
print(myinform)

doc = myinform.find()
print("doc: ", doc)

# corsur to json
json_data = dumps(list(doc))

with open("/Users/yong-gilhan/Desktop/School/4-1/시종설/github/practice/for-gilhan/information_of_naver.json", encoding='utf-8') as json_file:
		json_data = json.loads(json_file.read())


# print(json_data)
# print(json_data[0])
print(type(json_data))
print(type(json_data['Naver']))
data_list = json_data['Naver']



for a_info in data_list:
	myinform.insert_one(a_info)
	print(a_info)

# mydb.movies.insert_one(doc)

# print()

myclient.close()