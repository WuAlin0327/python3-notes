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
f = open("file.txt","r+")
file = f.read()
file = file.replace("喵喵喵","汪汪汪")
f.seek(0)
f.write(file)
f.close()
f2 = open("file.txt","r")
file2 = f2.read()
print(file2)
f2.close()