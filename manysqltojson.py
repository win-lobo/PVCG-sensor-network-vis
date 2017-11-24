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
sqls = "select * from 433mesh order by id desc limit 5"

while (1):
	resjson = []
	result = {}
	conn.commit();
	cur.execute(sqls)
#	print cur.rowcount
	rs = cur.fetchall()
	for eachitem in rs:
#		print type(eachitem),type(eachitem[0]),eachitem[0]
		result['id'] = int(eachitem[0])
		result['timestamp'] = eachitem[1].strftime('%Y-%m-%d %H:%M:%S')
		result['node_id'] = eachitem[2]
		result['temp'] = eachitem[3]
		result['humidity'] = eachitem[4]
		result['hops'] = eachitem[5]
		
#		for r in eachitem:
#			print type(r),r

		json_file = file(JSON_FILE, "w")			
		resjson = json.dumps(result)
#		print resjson
		json_file.writelines(resjson + os.linesep)
		json_file.close()
		time.sleep(UPDATE_INTERVAL)

cur.close()
conn.close()

