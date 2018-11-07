import pymysql
# # 建立连接
# conn = pymysql.connect(
# 	host='127.0.0.1',
# 	port=3306,
# 	user='root',
# 	password='123456',
# 	db='db5',
# 	charset='utf8'
# )
# # user = input('user >>>')
# # pwd = input('pwd >>>')
# # 拿到游标
# cursor = conn.cursor()
#
# # 执行sql语句
# #增删改，只需要将insert更换成对应语句即可
# sql = 'insert into userinfo(user,password) values (%s,%s)'
# # rows = cursor.execute(sql,('miao',321))#解决mysql注入问题
# rows = cursor.executemany(sql,[('wxx',123),('mxx',1234)]) # 插入多行
# conn.commit()# 提交
# # 关闭连接
# cursor.close()
# conn.close()
# if rows:
# 	print('111')
# else:
# 	print(rows)

import pymysql
conn = pymysql.connect(
	host='127.0.0.1',
	port=3306,
	user='root',
	password='123456',
	db='db4',
	charset='utf8'
)
cursor = conn.cursor(pymysql.cursors.DictCursor)# 以字典形式返回查询结果，调用cursor.fetchon打印出来的结果以字典形式打印
# 查询
cursor.callproc('p2',(2,4,0))
print(cursor.fetchall())
cursor.close()
conn.close()