#!/usr/bin/python

import MySQLdb
import time
import os
import json

UPDATE_INTERVAL = 10
JSON_FILE = "/var/www/433stream.json"


conn = MySQLdb.connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	passwd = 'helloworld',
	db = 'pvcgdb'
	)
#select * from 433mesh order by id desc limit 5
cur = conn.cursor()
sqls = "select * from 433mesh order by id desc limit 1"

while (1):
	resjson = []
	result = {}
	conn.commit()
	cur.execute(sqls)
	rs = cur.fetchone()
#	print type(rs),rs
#	print type(rs[0]),rs[0]
	result['id'] = rs[0]
	result['timestamp'] = rs[1].strftime('%Y-%m-%d %H:%M:%S')
	result['node_id'] = rs[2]
	result['temp'] = rs[3]
	result['humidity'] = rs[4]
	result['hops'] = rs[5]
	json_file = file(JSON_FILE, "w")
	resjson = json.dumps(result)
#	print(resjson)
	json_file.writelines(resjson + os.linesep)
	json_file.close()
	time.sleep(UPDATE_INTERVAL)

cur.close()
conn.close()

