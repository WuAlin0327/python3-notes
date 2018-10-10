'''
all() :如果列表中全部为True，返回True，只要有一个False则返回False
bool() : 判断一个类型是True或False
any() : 列表中任意一个值是True，则返回True
dir() :打印当前程序所有的变量
hex() :将一个数转成16进制
divmod() :传两个值进去返回两个值的整除与余数
sorted() :将列表从大到小排序# sorted(d.items(),key = lambda x:x[1.txt],reverse=True)
items() :将字典转换成列表
ascii() :返回ascii 码
oct() :将十进制转换成八进制
bin() :将十进制转换成二进制

eval() :将字符串公式转换成代码直接执行(按解释器规则)，可执行单行代码，有返回值
exec() :与eval干的事情是一样的，但是exec可执行多行，无返回值

'''

code = '''
def foo():
	print('run foo')
	return 1234
	
foo()
'''
res = exec(code)
print('res',res)
#>>> run fo
#>>> res None	exec无返回值