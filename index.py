#encoding=utf-8
import jieba
import jieba.posseg as pseg
from collections import Counter
# 用户字典 可自行添加专业名词 防止被jieba分错了
jieba.load_userdict('dict/user.dict')
# jieba.load_userdict('dict/dict.txt.big')
# 简体&繁体字典 这个不用修改,所以我让他当用户字典加载了
#jieba.set_dictionary('~/桌面/ji/dict/dict.txt.big')
# './a.txt'为想打开的文件
file_object = open('./源文件.txt','r',encoding="utf-8")
## 定义一个 list
L =list()
## 获取带词性的词对象（没学过py不知道得到的是什么）
words = pseg.cut(file_object.read())
i=0
## 遍历这个词对象
for word, flag in words:
	## 如果词性或者词属于这个范围就直接跳过 自己填写
	if flag=="x" or flag=="p"  or flag=="uj" or word=="年"or word=="月"or word=="日" :
		continue
	## 打印字符串 词和词性
	i=i+1
	print(i)
	##把词追加到list中
	L.append(word)
## 计算出现次数
getObj = Counter(L)
## 写到./getObj.json文件里
f = open('./getObj.json', 'w',encoding="utf-8")
f.write(str(getObj).replace("Counter(","").replace(")","").replace("'",'"'))
f.close()
file_object.close()
## end
