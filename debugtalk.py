import pymysql
import os
import random
import string
import json
import re
# 引入环境变量
backlogin = os.environ["backlogin"]           # admin
backpwd = os.environ["backpwd"]           # wsy88888
password = os.environ["password"]    # wsy888888
env = os.environ["env"]           
base_url = os.environ["base_url"]   

# 随机整型数字
def random_int(x,y=999999):
    return random.randint(x,y)

# 随机浮点型数字
def random_float(x,y=999999,k=4):
    return round(random.uniform(x,y),k)

# 随机字符
def random_str(x):
	ran_str = ''.join(random.sample(string.ascii_letters + string.digits, x))
	return ran_str

# 相加
def sum_two(x, y):
	x = float(x)
	y = float(y)
	return x + y

# 相乘
def mult_two(x,y):
	x = float(x)
	y = float(y)
	return x * y


# 取出最小的币种ID
def extract_change_rate(content_data):
	data = json.dumps(content_data)
	data_1 = json.loads(data)
	# return data_1['data'][3]['change_rate']
	l =[]
	for x in range(len(data_1)):
		s = data_1['data'][x]['change_rate']
		l.append(s)
	i = l.index(min(l))
	return data_1['data'][i]['id']

# 自动递增
def count_num(x):
	return x + 1

# 抽取权益卡密码
def card_pass(content_data):
	x = re.findall("密码：(\w{6})", content_data)
	return x[0]



# #创建连接
# conn = pymysql.connect(host="172.16.10.184", port=3313, user="root", password="tW2sDsVzD7Nae1jy",
#                        db="wsy_blockchain", charset='utf8')
# # 修改为888888
# def insetsql():
# 	cursor = conn.cursor()
# 	sql = 'UPDATE rights_card SET card_pass = \'45bdm2I/LOuviIJIvxwJp3eQACqpRYxaQ7n4Ob0upf/9LAg\' ORDER BY card_num DESC LIMIT 1;'
# 	try:
# 		# 执行sql语句
# 		cursor.execute(sql)
# 		conn.commit()
# 	except:
# 		conn.rollback()
# 		print("sql执行失败！")
# 	finally:
# 		cursor.close()
# 		conn.close()
# 		print("sql执行成功！")

# #查询权益卡ID
# def selecesql():
# 	cursor = conn.cursor()
# 	sql = 'SELECT * FROM rights_card ORDER BY card_num DESC LIMIT 1;'
# 	try:
# 		cursor.execute(sql)
# 		row_1 = cursor.fetchone()
# 	except:
# 		conn.rollback()
# 		print("sql执行失败！")
# 	finally:
# 		cursor.close()
# 		conn.close()
# 		print("sql执行成功！")
# 	return row_1[0]

