def range2(n):
	count = 0
	while count<n:
		print(count)
		count+=1
		yield count  #return   将函数变成生成器

new_range = range2(3)
next(new_range) #生成器调用语法

print("结束")

new_range.send("stop")

