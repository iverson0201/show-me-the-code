# -*- coding:utf-8 -*-
## 描述：把第二题所得的优惠券存储至MongoDB中。
### 引用：pymongo

import pymongo as mg

def save_to_mongodb() :
	cps = open("cps.txt","r+")
	conn = mg.Connection("localhost",27017)
	db = conn.ShowMeTheCode
	coupon = db.coupon
	i = 1
	for line in cps :
		coupon.insert({str(i): line[0:len(line) -1]})
		i = i+ 1
	conn.close()
	print("Well done.")

if __name__ == "__main__" :
	save_to_mongodb()