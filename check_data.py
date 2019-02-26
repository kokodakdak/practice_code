#coding:utf8
from pymongo import MongoClient
import datetime



client = MongoClient("10.10.10.172", 27017)
db = client.projects
project = "circle"

item = db[project].find_one({"name" : "배석대"})
item["text"] = "그는 철권을 못한다"
item["name"] = "배철권"
db[project].update_one({"name":"배석대"},{"$set": item}
