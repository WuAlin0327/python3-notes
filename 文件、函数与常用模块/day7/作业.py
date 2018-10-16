#
# li = [1,2,3,4,5,6,7,8,9]
# item = lambda i:
# print(item(li))
# def w1(func):
#     def inner():
#         print("before w1")
#         func()
#         print("after w1")
#     return inner
# def w2(func):
#     def inner():
#         print("before w2")
#         func()
#         print("after w2")
#     return inner
#
# @w1
# @w2
# def test():
#     print('test')
# test()
# def wrapper(flag):
#     def timer(func):
#         def inner(*args, **kwargs):
#             nonlocal flag
#             if flag:
#                 print('flag is active')
#             flag = func(*args, **kwargs)
#             if not flag:
#                 print('flag is down')
#             return flag
#         return inner
#     return timer
# @wrapper(True)
# def work():
#     print(111)
#     return False
# print(work())
# import re
# pattern = re.compile("o[gh]")
# p = pattern.fullmatch("dog")
# p2 = pattern.fullmatch("ohr")
# p3 = patter	n.fullmatch("og")
# p4 = pattern.fullmatch("doggie", 1, 3)
# print(p, p2, p3.group(), p4.group(), sep='\n')
# def range2(n):
#     count = 0
#     while count < n:
#         print(count)
#         count += 1
#         yield count
#
# new_range = range2(10)
# next(new_range)
# next(new_range)
# def range2(n):
#     count = 0
#     while count < n:
#         print(count)
#         count += 1
#         yield count
#     return 111
#
# new_range = range2(3)
# next(new_range)
# next(new_range)
# next(new_range)
# result = next(new_range)
# print(result)
# def work(n):
#     count = 0
#     while count < n:
#         count += 1
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
# res3 = new_range.send(False)
# print(res3)

from functools import wraps
def wrapper(func):
    def inner():
        print(func.__name__)
        return func()
    return inner

@wrapper
def work():
    return 123
print(work.__name__)
work()
