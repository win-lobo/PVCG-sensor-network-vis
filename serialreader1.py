#!/usr/bin/python

import random;
import MySQLdb;
import time;
import numpy;

UPDATE_INTERVAL = 5; 
NUM_NODES = 45;
MAX_HOPS = 5;

conn = MySQLdb.connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	passwd = 'helloworld',
	db = 'pvcgdb'
	);

cur = conn.cursor();
sqli = "insert into 433stream set node_id = %s, temp = %s, humidity = %s, hops = %s";

node_dict={2:30,3:33,4:19,5:9,6:40,7:44,8:13,9:29,10:1,11:12,12:33,13:20,14:15,15:10,16:1,17:27,18:44,19:29,20:9,21:17,22:38,23:38,24:29,25:45,26:32,27:34,28:34,29:16,30:1,31:32,32:34,33:1,34:1,35:12,36:17,37:27,38:37,39:30,40:20,41:12,42:30,43:10,44:10,45:19}
while (1):
	for node_id in xrange(2,NUM_NODES+1):
		hops_val=[]
		hops_val.append(node_id)
		while(hops_val[-1] != 1):
			hops_val.append(node_dict[hops_val[-1]])
		hops_str = ','.join(map(str, hops_val))
		#print hops_str
		temp = random.uniform(20, 30)
	        humidity = random.uniform(60, 90)
		cur.execute(sqli, ('%d'%node_id, '%.2f'%temp,'%.2f'%humidity, '%s'%hops_str))
		conn.commit()
		time.sleep(UPDATE_INTERVAL)

cur.close();
conn.close();

