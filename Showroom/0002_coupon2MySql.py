# -*- coding:utf-8 -*-
## 描述：将上题产生的优惠券存入MySql中。
### 注意：使用Python3.4；依赖PyMysql模块。

import pymysql as mydb

def save_coupon_to_mysql() :
	cp_file = open("cps.txt","r+")
	git_db = mydb.connect(
		host="localhost",
		port=3306,
		user="root",
		passwd="root",
		db="ShowMeTheCode"
	)
	cur = git_db.cursor()
	for line in cp_file :
		try :
			cur.execute("Insert into Coupon(id) values('{0}');".format(line[0:len(line)-1]))
			git_db.commit()
		except Exception :
			git_db.rollback()
		print("Inserted >>>" +line[0:len(line)-1])
	git_db.close()
	print("Well done.")
	return True

if __name__ == "__main__" :
	save_coupon_to_mysql()