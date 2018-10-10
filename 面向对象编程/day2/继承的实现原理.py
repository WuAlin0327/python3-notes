#1.txt.新式类


#2.经典类

#在python2中 经典类：每有继承object的类，以及它的子类都称之为经典类
'''
class Foo:
	pass
class Bar(Foo):
	pass
'''
#在python2中 新式类：继承object的类，以及它的子类都称之为新式类
'''
class Foo(object):
	pass
class Bar(Foo)
	pass

'''
# 在python3中新式类：默认继承object
class Foo:
	pass
print(Foo.__bases__)