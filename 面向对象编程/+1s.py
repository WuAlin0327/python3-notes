import pymysql
import time
import random
import string

conn = pymysql.connect(
		host='127.0.0.1',
		port=3306,
		user='root',
		password='123456',
		db='db2',
		charset='utf8'
	)

cursor = conn.cursor()

name_list = ['wualin','alex','egon','xiaoma','zhangzz']

for name in name_list:
	password = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
	sql = "insert into t2(username,password) values ('%s','%s')"%(name,password)
	print(sql)
	cursor.execute(sql)

conn.commit()
conn.close()
cursor.close()