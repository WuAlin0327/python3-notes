import tabulate
import os

FILENAME = 'staff_table.txt'
DATA = ['id','name','age','phone','career','date']
FUNC = ['find','add','updata','del']
def staff_data():
	'''
	数据结构
	:return:
	'''
	f = open(FILENAME,'r')

	staff = {
		'id':[],
		'name':[],
		'age':[],
		'phone':[],
		'career':[],
		'date':[]
	}
	file = f.readlines()
	for i in file:
		staff['id'].append(i.strip().split(',')[0])
		staff['name'].append(i.strip().split(',')[1])
		staff['age'].append(i.strip().split(',')[2])
		staff['phone'].append(i.strip().split(',')[3])
		staff['career'].append(i.strip().split(',')[4])
		staff['date'].append(i.strip().split(',')[5])
	f.close()
	return staff
STAFF_DATA = staff_data()

def save_data(data):
	'''
	保存数据
	:return:
	'''
	save_all = []
	for index,l in enumerate(data['id']):
		snap = []
		for i in DATA:
			snap.append(STAFF_DATA[i][index])
		save_all.append(snap)
	f = open('%s.new'%FILENAME,'w')
	for i in save_all:
		f.write(','.join(i)+'\n')
	f.close()
	os.rename('%s.new'%(FILENAME),FILENAME)
def del_data():
	'''
	删除数据
	:return:
	'''

def big(decide,condition,res_data):# 大于
	'''

	:param decide: 条件前置 eg. age > 22
	:param condition: 条件 eg. 22
	:param res_data: 解析find后面是什么，find *  or find name,age
	:return:
	'''


	if res_data != '*':
		snap = []
		for i in STAFF_DATA[decide]:
			if int(i) > int(condition):
				index_big = STAFF_DATA[decide].index(i)
				snap_1 = []
				for k in res_data:
					snap_1.append(STAFF_DATA[k][index_big])
				snap.append(snap_1)
		print(tabulate.tabulate(snap,headers=(i for i in res_data)))
		print("查询到了%s 条记录" % (len(snap)))
	else:
		p_all = []
		for i in STAFF_DATA[decide]:
			if int(i) > int(condition):
				index_big = STAFF_DATA[decide].index(i)
				snap = []
				for k in DATA:
					snap.append(STAFF_DATA[k][index_big])
				p_all.append(snap)
		print(tabulate.tabulate(p_all,headers=(i for i in DATA)))
		print("查询到了%s 条记录" % (len(p_all)))

def small(decide,condition,res_data):# 小于


	if res_data != '*':
		snap = []
		for i in STAFF_DATA[decide]:
			if int(i) < int(condition):
				index_big = STAFF_DATA[decide].index(i)
				snap_1 = []
				for k in res_data:
					snap_1.append(STAFF_DATA[k][index_big])
				snap.append(snap_1)
		print(tabulate.tabulate(snap,headers=(i for i in res_data)))
		print("查询到了%s 条记录" % (len(snap)))
	else:
		p_all = []
		for i in STAFF_DATA[decide]:
			if int(i) < int(condition):
				index_big = STAFF_DATA[decide].index(i)
				snap = []
				for k in DATA:
					snap.append(STAFF_DATA[k][index_big])
				p_all.append(snap)
		print(tabulate.tabulate(p_all,headers=(i for i in DATA)))
		print("查询到了%s 条记录" % (len(p_all)))
def equal(decide,condition,res_data):# 等于
	snap = []

	for i in STAFF_DATA[decide]:

		if i == condition:
			index_big = STAFF_DATA[decide].index(i)
			snap_1 = []
			for k in DATA:
				snap_1.append(STAFF_DATA[k][index_big])
			snap.append(snap_1)
	print(tabulate.tabulate(snap, headers=(i for i in DATA)))
	print("查询到了%s 条记录"%(len(snap)))
def like(decide,condition):# 相似
	snap = []

	for i in STAFF_DATA[decide]:
		if condition in i:
			index_big = STAFF_DATA[decide].index(i)
			snap_1 = []
			for k in DATA:
				snap_1.append(STAFF_DATA[k][index_big])
			snap.append(snap_1)
	print(tabulate.tabulate(snap,headers=(i for i in DATA)))
	print("查询到了%s 条记录"%(len(snap)))

def print_all():# 打印所有
	p_all = []
	for index,l in enumerate(STAFF_DATA['id']):
		snap = []
		for i in DATA:
			snap.append(STAFF_DATA[i][index])
		print(snap)

def syntax_add(cmd):
	add_info = cmd.strip().split()[2:]

	if add_info[2] not in STAFF_DATA['phone']:

		STAFF_DATA['id'].append(str(len(STAFF_DATA['id'])+1))
		STAFF_DATA['name'].append(add_info[0])
		STAFF_DATA['age'].append(add_info[1])
		STAFF_DATA['phone'].append(add_info[2])
		STAFF_DATA['career'].append(add_info[3])
		STAFF_DATA['date'].append(add_info[4])
		save_data(STAFF_DATA)
		print("增加了1条数据")
	else:
		print('该phone 已存在，无法添加')



def syntax_find(cmd):
	'''
	传入输入的语句，解析语句
	:param cmd:
	:return:
	'''
	where_left,where_right = cmd.split('where')
	calculation = {
		'>': big,
		'<': small,
		'=': equal,
		'like': like
	}
	if where_left.split()[0] in FUNC:
		resovle = where_left.split()

		if where_right.split()[0] in DATA:
			where_right = where_right.strip().split()
			if resovle[1]=='*':
				res = '*'
				for k in calculation:
					if where_right[1] == k:
						calculation[k](where_right[0],where_right[2],res,)# 如果find后面是'*'号则
			else:
				res = resovle[1].split(',')
				for k in calculation:
					if where_right[1] == k:
						calculation[k](where_right[0],where_right[2],res,)# 执行对应函数
		else:
			print("%s 不在%s"%(where_right.split[0],(i for i in DATA)))
	else:
		print("语法错误")


def main():
	while True:
		cmd = input('>>>')
		if cmd.strip().split()[0]== 'find':
			syntax_find(cmd.strip())
		if cmd.strip().split()[0]=='add':
			syntax_add(cmd)

main()