# python基础语法

### 变量与常量
声明变量：

```
name = "wualin"
```

##### 变量的定义规则：
1.
变量名只能是字母，数字，下划线的任意组合
2.
变量名的第一个字符不能是数字
3.
关键字不能声明为变量名

常量：常量即指不变的量，如pai
3.141592653..., 或在程序运行过程中不会改变的量
程序员约定俗成常量命名为大写字母

#### 程序交互：
读取用户输入

```
name = input("What is your name?")

print("Hello " + name)
```

以上程序会在输入后继续执行

#### 注释：代码注释分单行和多行注释， 单行注释用#，多行注释可以用三对双引号""" """


## 基本数据类型：
#### 数字类型：
python3只有两种数字类型
1.
整型int()
2.
浮点型float()

#### 字符串类型
在Python中, 加了引号的字符都被认为是字符串。单引号和双引号没有任何区别
三引号用于多行字符串
字符串可以使用相加与相乘运算：

```
>> > name
'Alex Li'
>> > age
'22'
>> > name + age  # 相加其实就是简单拼接
'Alex Li22'
>> > name * 10  # 相乘其实就是复制自己多少次，再拼接在一起
'Alex LiAlex LiAlex LiAlex LiAlex LiAlex LiAlex LiAlex LiAlex LiAlex Li'
```

++字符串拼接只能是字符串与字符串拼接，不允许跟其他数据类型拼接 + +

#### 布尔型（bool）
布尔类型：True（真）  False（假），主要用于逻辑判断，例：

```
if a > b

	print(a is bigger
	than
	b )

	else

	print(a is smallerthan b )
```

#### 格式化输出

```
	name = input("Name")
	age = input("Age")
	job = input("Job")
	hometwon = input("Hometwon")

	info = '''
----------info of %s ----------- 
Name			: %s
Age				: %s
Job				: %s
Hometwon		: %s
----------end------------------- 
''' % (name, name, age, job, hometwon)
	# %s = string
	# %d = difit
	# %f = float
	print(info)
	"""
```
info of %s中的%s就是一个占位符，这一行中的代表后面%（中的第一个）
%s在没有要求必须是数字或者小数的情况下是万能的
	
