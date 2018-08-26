# 智能检测文件编码
# import chardet
# f = open("file.txt","rb")
# date = f.read
# date = chardet.detect(date)
# print(date)
# import chardet
# f = open("file.txt",mode='rb')
# data = f.read()
# f.close()
#
# result = chardet.detect(open('file.txt',mode='rb').read())
# print(result)
#
## 循环读取文件（每次读一行）
# f = open("file.txt","r",encoding="utf-8")
#
# for line in f:
# 	print(line)
# f.close()