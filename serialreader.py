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

all_nodes = numpy.arange(2, NUM_NODES + 1);
while (1):
	node_id = random.randint(2, NUM_NODES);
	temp = random.uniform(20, 30);
	humidity = random.uniform(60, 90);
	hops_val = random.sample(all_nodes, random.randint(1, MAX_HOPS - 2));
	hops_val.append(1);
	hops_val.insert(0, node_id);
	hops_str = ','.join(map(str, hops_val));
	cur.execute(sqli, ('%d'%node_id, '%.2f'%temp,'%.2f'%humidity, '%s'%hops_str));
	conn.commit();
	time.sleep(UPDATE_INTERVAL);

cur.close();
conn.close();

