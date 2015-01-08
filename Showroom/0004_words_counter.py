# -*- coding: utf-8 -*-
## 描述：统计单词的出现个数
### 

import re

def  counter(path):
	post = open(path)
	wc = {}
	for line in post :
		words = re.split(r"[.,;! \?@:\"“”/]", line)	#根据匹配正则表达式的字符串切割
		for word in words :
			word = word.lower()
			wc[word] = wc.setdefault(word, 0)+1	#setdefault方法：存在时，返回值；不存在时，先设置默认值再返回。
	for (w,c) in wc.items() :
		print(w+':'+str(c), end='\t')

if __name__ == "__main__" :
	counter("paragraph.txt")