import logging
import sys
import time
import sqlite3
#from sqlite3 import Error
import threading
import asyncio
import json

from simple_websocket_server import WebSocketServer, WebSocket

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
	
	def handle(self):
		sockdata = json.loads(self.data)
		
		conn = sqlite3.connect('file:antrean.db')
		cur = conn.cursor()
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

	def connected(self):
		clients.append(self)

	def handle_close(self):
		clients.remove(self)

# broadcast message every n seconds defined in config (delay)
def loops():
	conn = sqlite3.connect('file:antrean.db')
	conn.row_factory = sqlite3.Row
	cur = conn.cursor()
	cur.execute("select count(*) from antrean")
	cnt = cur.fetchone()[0]
	
	if int(cnt) > 0:
		cur.execute("select id, data from antrean order by id asc limit 1")
		data = cur.fetchone()
		#print(data['data'] + " " + str(data['id'])) 

		#broadcast
		for client in clients:
			client.send_message(data['data'])
		#delete current data
		cur.execute("delete from antrean where id=" + str(data['id']))
		conn.commit()
	conn.close()
	threading.Timer(int(delay), loops).start()

loops()

server = WebSocketServer(socketserver, socketport, teraWebSocket)
server.serve_forever()