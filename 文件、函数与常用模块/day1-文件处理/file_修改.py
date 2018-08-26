# 占用硬盘方式：
# import os
# f_name = "file.txt"
# f_new = "%s.new"%f_name
#
# old_str = "喵喵喵"
# new_str = "汪汪汪"
#
# f1 = open(f_name,"r")
# f2 = open(f_new,"w")
# for line in f1:
# 	if old_str in line:
# 		line = line.replace(old_str,new_str)
# 	f2.write(line)
# f1.close()
# f2.close()
#
# os.rename(f_new,f_name)#使用os模块用新文件替换旧文件

# 占用内存方式
f = open("file.txt","r+")
file = f.read()
file = file.replace("汪汪汪","喵喵喵")
f.seek(0)
f.write(file)
f.close()
f2 = open("file.txt","r")
file2 = f2.read()
print(file2)
f2.close()
