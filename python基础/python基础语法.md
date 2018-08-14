# python基础语法

### 变量与常量
声明变量：

```
name = "wualin"
```

##### 变量的定义规则：
1. 变量名只能是字母，数字，下划线的任意组合
2. 变量名的第一个字符不能是数字
3. 关键字不能声明为变量名

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


### 基本数据类型：
#### 数字类型：
python3只有两种数字类型
1. 整型int()
2. 浮点型float()

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
if a > b：
    print(a is bigger than b )

else：
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
Age			: %s
Job			: %s
Hometwon		: %s
----------end------------------- 
''' % (name, name, age, job, hometwon)
# %s = string
# %d = difit
# %f = float
print(info)
```
info of %s中的%s就是一个占位符，这一行中的代表后面%（中的第一个）

%s在没有要求必须是数字或者小数的情况下是万能的

### 运算符
* 算数运算
* 比较运算
* 逻辑运算
* 赋值运算
* 成员运算
* 身份运算
* 位运算

##### 算数运算
假设x = 10，y = 20

运算符 | 描述
-----|-----
\+ | 加-两个对象相加
\- | 减-得到负数或者一个数减去另一个数
\* | 乘-两个数相乘或返回一个被重复若干次的字符串
\/ | 除-x除以y
\% | 取模-返回除法的余数
\** | 幂-返回x的y次幂
\// | 返回商的整数部分

##### 比较运算
假设变量x = 10，y = 20

运算符 | 描述
----- | -----
== | 等于-比较对象是否相等
！= | 不等于-比较两个对象是否不想等
\>  |  大于-返回x是否大于y
\<  |  小于-返回x是否小于y
\>=  |  大于等于-返回x是否大于等于y
\<=  |  小于等于-返回x是否小于等于y

##### 赋值运算
假设变量x = 10，b = 20

运算符 | 描述
---|---
\=|简单的赋值运算符
+= |加法赋值运算符（c+=a等效与c=c+a）
-= |减法赋值运算符
*= |乘法赋值运算符
/= |除法赋值运算符
%= |取模赋值运算符
**=|幂赋值运算符
//=|取整数赋值运算符

##### 逻辑运算
运算符 | 描述
---|---
and |与-如果x为false，x and y返回false，否则它返回y的计算值
or |或-如果x是true，它返回true，否则它返回y的计算值。
not |非-如果x为true，返回false。如果x为false，它返回true

##### 逻辑运算

---

### 流程控制
* 单分支
* 双分支
* 多分支

##### 单分支

```
if 条件：
    满足条件后执行的代码
```
##### 双分支

```
if 条件：
    满足条件后执行的代码
else：
    if条件不满足执行的代码
```
##### 多分支

```
if 条件：
    满足条件后执行的代码
elif 条件：
    上面条件不满足就执行这代码
else：
    上面条件都不满足就执行这段
```

---
### while循环
##### 语法：

```
while 条件：
    执行代码。。。
```
使用while循环打印1-100:

```
ount = 0
while count <= 100:
	print("loop",count)
	count+=1

```
##### 死循环
while循环只要后面条件成立（也就是结果为真）就一直执行

例：

```
while True:
	print("死循环")
```
##### 循环终止语句
* break：用于完全结束一个循环，跳出循环体执行循环后面的语句
* continue：与break类似，区别在于continue只是终止本次循环，接着还执行后面的循环，break则完全终止

break：

```
count = 0
while count <= 100:
	print("loop",count)
	if count == 5:
		continue
	count+=1

print("----end----")
```
continue：

```
count = 0
while count <= 100:
	print("loop",count)
	if count == 5:
		continue
	count+=1

print("----end----")
```
##### while else
while后面的else作用是指，当while循环正常执行完，中间没有被break终止的花，就会执行else后面的语句

###### 作用：用来测试循环是否执行完毕，判断循环是否有异常




	
