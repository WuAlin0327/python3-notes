# def w1(func):
# 	def inner():
# 		print("before w1")
# 		func()
# 		print("after w1")
# 	return inner
# def w2(func):
# 	def inner():
# 		print("before w2")
# 		func()
# 		print("after w2")
# 	return inner
#
# @w1
# @w2
# def test():
# 	print('test')
# test()
#
# from functools import wraps
# def wrapper(func):
#
# 	def inner():
# 		print(func.__name__)
# 		return func()
# 	return inner
# @wrapper
# def worj():
# 	return 123
# print(worj.__name__)
# worj()
# g = (i for i in range(5))
# for j in g:
#     if j >= 2:
#         print(list(g))
#     print(j)
# def work(n):
#     count = 0
#     while count < n:
#         count += 1.txt
#         sign = yield count
#         if not sign:
#             yield count+2
#
# new_range = work(4)
# res = next(new_range)
# print(res)
# res1 = new_range.send(True)
# print(res1)
# res2 = new_range.send(False)
# print(res2)

def work(n):
    count = 0
    while count < n:
        count += 1
        sign = yield count
        if sign:
            break
    yield "over"

new_range = work(5)
res = next(new_range)
res1 = new_range.__next__()
res2 = new_range.send(True)
print(res, res1, res2, sep=' ')
next(new_range)




