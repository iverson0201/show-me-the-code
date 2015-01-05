# -*- coding:utf-8 -*-
## 描述：生成优惠券
### 输出：见cps.txt文件

import uuid

def gen_coupon() :
	return str(uuid.uuid4())

def save_coupon(count) :
	cpfile = open("cps.txt","w+")
	for i in range(count) :
		cpfile.write(gen_coupon()+'\n')
	cpfile.close()
	print "Finished."

if __name__ == "__main__" :
	num = (int)(raw_input("How many coupons you want to generate?"))
	save_coupon(num)