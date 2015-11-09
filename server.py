import threading
import socket
import time
import sys

def get_file(nama):
	myfile = open(nama)
	return myfile.read()

class MemprosesClient(threading.Thread):
	def __init__(self,client_socket,client_address,nama):
		self.client_socket = client_socket
		self.client_address = client_address
		self.nama = nama
		threading.Thread.__init__(self)

	def run(self):
		message = ''
		while True:
			data = self.client_socket.recv(32)
			if data:
				message = message + data 
				#print message
				#collect seluruh data yang diterima
				if (message.endswith("\r\n\r\n")):
					#print 'Client finish'
					self.client_socket.send('HTTP/1.1 200 OK\r\n\r\n'+get_file('gambar.jpg'))
					#self.client_socket.send('HTTP/1.1 200 OK\r\n\r\ntes')
					break
			else:
				break
		self.client_socket.close()

class Server(threading.Thread):
	def __init__(self):
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server_address = ('127.0.0.1',9999)
		self.my_socket.bind(self.server_address)
		threading.Thread.__init__(self)
		print 'Server is running!'

	def run(self):
		self.my_socket.listen(1)
		nomor=0
		while (True):
			self.client_socket, self.client_address = self.my_socket.accept()
			#print 'Another client is connecting'
			nomor=nomor+1
			#---- menghandle message cari client (Memproses client)
			my_client = MemprosesClient(self.client_socket, self.client_address, 'PROSES NOMOR '+str(nomor))
			my_client.start()
			
#----
serverku = Server()
serverku.start()
