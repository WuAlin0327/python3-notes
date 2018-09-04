FILENAME = 'staff_table.txt'
DATA = ['id','name','age','phone','career','date']

def staff_data():
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
def add_staff(func):
	i = func.strip().split(' ')
	number = len(staff_data()['id'])
	s = ','.join(i[1:])
	f = open(FILENAME,'r+')
	f.read()
	f.write('\n'+str(number)+','+s)
	f.close()
def func():
	pass


def main():
	s_canf = input('>>>')
	lis = []
	lis.append(s_canf.strip().split(' '))
	return lis
s_canf = input('>>>')
add_staff(s_canf)