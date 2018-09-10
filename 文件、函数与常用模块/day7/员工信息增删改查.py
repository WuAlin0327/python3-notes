import tabulate
import os

FILENAME = 'staff_table.txt'
DATA = ['id','name','age','phone','dept','date']
FUNC = ['find','add','update','del']
def staff_data():
	'''
	打开文件将文件内容输出为以字典形式的数据结构
	:return:
	'''
	f = open(FILENAME,'r')

	staff = {
		'id':[],
		'name':[],
		'age':[],
		'phone':[],
		'dept':[],
		'date':[]
	}
	file = f.readlines()
	for i in file:
		staff['id'].append(i.strip().split(',')[0])
		staff['name'].append(i.strip().split(',')[1])
		staff['age'].append(i.strip().split(',')[2])
		staff['phone'].append(i.strip().split(',')[3])
		staff['dept'].append(i.strip().split(',')[4])
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
def syntax_del(cmd):
	'''
	删除数据
	:return:
	'''
	snap = []
	c_del = cmd.split()[-1].strip()
	for index,i in enumerate(STAFF_DATA['id']):
		snap_1 = []
		if i == c_del:
			l = index
			for s in DATA:
				snap_1.append(STAFF_DATA[s][l])
				del STAFF_DATA[s][l]
			snap.append(snap_1)
			save_data(STAFF_DATA)
			print("删除了1条数据"+'\n',tabulate.tabulate(snap,headers=(i for i in DATA)))



def big(decide,condition,res_data):# day1
	'''

	:param decide: 条件前置 eg. age > 22
	:param condition: 条件 eg. 22
	:param res_data: 解析find后面是什么，find *  or find name,age
	:return:
	'''


	if res_data != '*':
		snap = [] #临时变量
		for i in STAFF_DATA[decide]:
			if int(i) > int(condition):
				index_big = STAFF_DATA[decide].index(i)
				snap_1 = []
				for k in res_data:
					snap_1.append(STAFF_DATA[k][index_big])
				snap.append(snap_1)
		print("查询到了%s 条记录" % (len(snap)))
		print(tabulate.tabulate(snap,headers=(i for i in res_data)))

	else:
		snap = []
		for i in STAFF_DATA[decide]:
			if int(i) > int(condition):
				index_big = STAFF_DATA[decide].index(i)
				snap_1 = []
				for k in DATA:
					snap.append(STAFF_DATA[k][index_big])
				snap.append(snap_1)

			print("查询到了%s 条记录" % (len(snap)))
			print(tabulate.tabulate(snap,headers=(i for i in DATA)))


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
		print("查询到了%s 条记录" % (len(snap)))
		print(tabulate.tabulate(snap,headers=(i for i in res_data)))
	else:
		snap = []
		for i in STAFF_DATA[decide]:
			if int(i) < int(condition):
				index_big = STAFF_DATA[decide].index(i)
				snap_1 = []
				for k in DATA:
					snap.append(STAFF_DATA[k][index_big])
				snap.append(snap_1)
		print("查询到了%s 条记录" % (len(snap)))
		print(tabulate.tabulate(snap,headers=(i for i in DATA)))

def equal(decide,condition,res_data):# 等于
	snap = []
	for index,i in enumerate(STAFF_DATA[decide]):
		if i == condition:
			index_equal = index
			snap_1 = []
			if i == condition:

				for k in DATA:
					snap_1.append(STAFF_DATA[k][index_equal])
				snap.append(snap_1)
	print(tabulate.tabulate(snap, headers=(i for i in DATA)))
	print("查询到了%s 条记录"%(len(snap)))
def like(decide,condition,res_data):# 相似
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

def syntax_add(cmd): # 增加
	add_info = cmd.strip().split()[2:]

	if add_info[2] not in STAFF_DATA['phone']:

		STAFF_DATA['id'].append(str(len(STAFF_DATA['id'])+1))
		STAFF_DATA['name'].append(add_info[0])
		STAFF_DATA['age'].append(add_info[1])
		STAFF_DATA['phone'].append(add_info[2])
		STAFF_DATA['dept'].append(add_info[3])
		STAFF_DATA['date'].append(add_info[4])
		save_data(STAFF_DATA)
		print("增加了1条数据")
	else:
		print('该phone 已存在，无法添加')



def syntax_find(cmd): # 查找
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
		print("语法错误")

def syntax_update(cmd):#修改数据
	'''
	解析输入更新语句，获取需要修改的值，然后用新值替换后写入文件
	:param cmd:
	:return:
	'''
	res1_cmd,res2_cmd = cmd.strip().split('where')
	old_res = res2_cmd.split('=')
	new_res = res1_cmd.split('set')[-1].split('=')
	snap = []
	for index,i in enumerate(STAFF_DATA[old_res[0].strip()]):
		if i == old_res[-1].strip():
			snap.append(index)
			index = index
			STAFF_DATA[new_res[0].strip()][index] = new_res[-1].strip()
	print("修改了%s条记录！"%(len(snap)))
	save_data(STAFF_DATA)


def main():
	while True:
		STAFF_DATA = staff_data()
		cmd = input('>>>')
		if 'where' in cmd.strip().split():
			if cmd.strip().split()[0]=='find':
				syntax_find(cmd)
			if cmd.strip().split()[0]=='update':
				syntax_update(cmd)

		if cmd.strip().split()[0]=='add':
			syntax_add(cmd)
		if cmd.strip().split()[0]=='del':
			syntax_del(cmd)
		elif cmd.strip().split()[0] not in FUNC:
			print("语句必须以'find','del','add','update'开头！")

main()