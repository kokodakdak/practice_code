#coding:utf8
import redis


r = redis.Redis(host='10.10.10.172', port=6379)
for i in range(1000000):
	r.set("baeseoyoung","배석대" +str(i))
print r.get("baeseoyoung")
