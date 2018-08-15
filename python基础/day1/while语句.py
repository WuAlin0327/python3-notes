"""count = 0
while count <= 100:
	print("loop",count)
	count+=1
"""


"""
#打印偶数
count = 0
while count <= 100:
	if count % 2 == 0:
		print("loop",count)
	count+=1
"""


"""
#第50次不打印，第60-80打印对应值的平方

count = 0
while count <=100:
	if count == 50:
		pass
	elif count >= 60 and count <= 80:
		print(count*count)
	else:
		print(count)
	count+=1

print("end")
"""
"""
#死循环
while True:
	print("死循环")
"""
count = 0
while count <= 100:
	print("loop",count)
	if count == 5:
		continue
	count+=1

print("----end----")
