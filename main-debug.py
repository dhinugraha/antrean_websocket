#!/usr/bin/env python
import sys
import sqlite3
from datetime import datetime
import threading
import json

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

if (sys.version_info > (3, 0)):
	import configparser
	config = configparser.ConfigParser()
	config.read('config.txt')
else:
	import ConfigParser
	config = ConfigParser.ConfigParser()
	config.read(r'config.txt')

delay = config.get("config", "delay")
socketserver = config.get("config", "server")
socketport = config.get("config", "port")

clients = []

class teraWebSocket(WebSocket):
	
	def handleMessage(self):
		sockdata = json.loads(self.data)
		
		conn = sqlite3.connect('antrean.db')
		cur = conn.cursor()
		print(datetime.now())
		print("accept new data : " + self.data)
		print("----------------")
		if "reset" in sockdata:
			#reset sequence
			cur.execute("UPDATE SQLITE_SEQUENCE SET SEQ= 0 WHERE NAME='antrean'")
			conn.commit()
			#delete data
			cur.execute("delete from antrean")
			conn.commit()
		else:
			#accept data antrean
			cur.execute("INSERT INTO antrean(data) VALUES('" + self.data + "')")			
			conn.commit()
		conn.close()

	def handleConnected(self):
		print(self.address[0] + " connected")
		print("-----------------")
		clients.append(self)

	def handleClose(self):
		clients.remove(self)
		print(self.address, 'closed')
		print("-----------------")

# broadcast message every n seconds defined in config (delay)
def loops():
	conn = sqlite3.connect('antrean.db')
	conn.row_factory = sqlite3.Row
	cur = conn.cursor()
	cur.execute("select count(*) from antrean")
	cnt = cur.fetchone()[0]
	
	if int(cnt) > 0:
		cur.execute("select id, data from antrean order by id asc limit 1")
		data = cur.fetchone()
		print("broadcast : " + data['data'] + " " + str(data['id'])) 

		#broadcast
		for client in clients:
			client.sendMessage(data['data'])
		#delete current data
		cur.execute("delete from antrean where id=" + str(data['id']))
		conn.commit()
	else:
		print("no data")

	conn.close()
	threading.Timer(int(delay), loops).start()

loops()

server = SimpleWebSocketServer(socketserver, socketport, teraWebSocket)
server.serveforever()