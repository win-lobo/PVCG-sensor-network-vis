#!/usr/bin/python

import MySQLdb;
import time;
from datetime import datetime, timedelta;
import json;

UPDATE_INTERVAL = 5; 
JSON_FILE = "/var/www/433stream.json";


conn = MySQLdb.connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	passwd = 'helloworld',
	db = 'pvcgdb'
	);
#select * from 433mesh order by id desc limit 5
cur = conn.cursor();
sqls = "select * from 433stream where tstamp >= %s and tstamp <= %s order by node_id limit 1";

while (1):
	resjson = [];
	result = {};
	end_time = datetime.now();
	start_time = end_time - timedelta(seconds = UPDATE_INTERVAL); 
	cur.execute(sqls, 
		(start_time.strftime('%Y-%m-%d %H:%M:%S'), 
		end_time.strftime('%Y-%m-%d %H:%M:%S')));
	conn.commit();
	rs = cur.fetchall();
	json_file = file(JSON_FILE, "w");
	for r in rs:
		result['id'] = r[0];
		result['timestamp'] = r[1].strftime('%Y-%m-%d %H:%M:%S');
		result['node_id'] = r[2];
		result['temp'] = r[3];
		result['humidity'] = r[4];
		result['hops'] = r[5];
		resjson = json.dumps(result);	
		print(resjson);
		json_file.writelines(resjson + "\n");
	json_file.close();
	time.sleep(UPDATE_INTERVAL);

cur.close();
conn.close();

