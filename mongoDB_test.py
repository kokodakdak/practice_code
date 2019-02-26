#coding:utf8
from pymongo import MongoClient
import datetime


client = MongoClient("10.10.10.172", 27017)
db = client.projects
project = "circle"
date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
item = {"name":"배석대",
		"text":"소속이 어떻게 되시죠?",
		"tags": ["무력", "강압","권력","화","그는 학원 원장님"],
		"date": date,
}
db["circle"].insert_one(item)
