import logging
import sys
import time
import queue
from datetime import datetime

from simple_websocket_server import WebSocketServer, WebSocket

if (sys.version_info > (3, 0)):
	import configparser
	config = configparser.ConfigParser()
	config.read('config.txt')
else:
	import ConfigParser
	config = ConfigParser.ConfigParser()
	config.read(r'config.txt')

class teraWebSocket(WebSocket):
	
	def handle(self):
		delay = config.get("config", "delay")
		print("message for " + self.request.path + " group : " + self.data)
		print(datetime.now())
		print("-----------------")
		for client in clients:
			if client.request.path == self.request.path:
				if client != self:
					client.send_message(self.data)
					#time.sleep(int(delay))

	def connected(self):
		print(self.request.path + " " + self.address[0] + " connected")
		print("-----------------")
		clients.append(self)

	def handle_close(self):
		clients.remove(self)
		print(self.address, 'closed')
		print("-----------------")
		#for client in clients:
		#    client.send_message(self.address[0] + u' - disconnected')

clients = []

logger = logging.getLogger('websockets.server')
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler())

socketserver = config.get("config", "server")
socketport = config.get("config", "port")

server = WebSocketServer(socketserver, 8000, teraWebSocket)
server.serve_forever()