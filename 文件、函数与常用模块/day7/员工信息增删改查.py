lis = []
dic = {}
f = open('staff_table.txt','r')
for i in f.readlines():
	lis.append(i.strip().split(','))
for i in lis:
	dic[int(i[0])] = i[1:]
def info(n):
	name = dic[n][0]
	age = dic[n][1]
	phone = dic[n][2]
	career = dic[n][3]
	date = dic[n][4]
	return [name,age,phone,career,date]

def find(args):
	for i in range(1,11):
		if args in info(i):
			print(info(i))
find('22')
