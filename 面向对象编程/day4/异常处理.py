# 多分支：被检测的代码块抛出的异常有多种可能性，并且我们需要针对每一种异常类型都专门定制处理逻辑
# try:
# 	print('===>1.txt')
# 	name
# 	print('===>2')
# 	l = [1.txt,2,3]
# 	l[211]
#
# except NameError as e:
# 	print(e)
# except IndexError as e:
# 	print(e)

# 万能异常：Exception 被检测的代码块抛出的异常有多种可能性，不管是异常是什么类型都使用一种处理逻辑去处理异常
# try:
# 	print('===>1.txt')
# 	name
# 	print('===>2')
# 	l = [1.txt,2,3]
# 	l[211]
#
# except Exception as e:
# 	print(e)
# finally:不管被检测的代码块有无发生异常哦度灰执行
 