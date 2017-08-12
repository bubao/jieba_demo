#encoding=utf-8
import codecs
# gbk转utf8脚本
def ReadFile(filePath,encoding="gb18030"):
    with codecs.open(filePath,"r",encoding) as f:
        return f.read()
def WriteFile(filePath,u,encoding="utf-8"):
    with codecs.open(filePath,"w",encoding) as f:
        f.write(u)
def UTF8_2_GBK(src,dst):
    content = ReadFile(src,encoding="gb18030")
    WriteFile(dst,content,encoding="utf-8")

UTF8_2_GBK("./all.txt","./a.txt")