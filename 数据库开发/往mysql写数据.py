import pymysql
import random
conn = pymysql.connect(
	host='127.0.0.1',
	port=3306,
	user='root',
	password='123456',
	db='homework',
	charset='utf8'
)
coursor = conn.cursor()
count = 0
while count < 20:
	student_id = random.randint(1,11)
	course_id = random.randint(1,7)
	score = random.randint(0,100)
	sql = 'insert into score (student_id,course_id,score) values (%s,%s,%s)'%(student_id,course_id,score)
	print(sql)
	coursor.execute(sql)
	count+=1
	conn.commit()


coursor.close()
conn.close()