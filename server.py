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
					print message
					arraymessage = message.split(' ',2)
					print arraymessage[1]
					if arraymessage[1]=="/gambar1":
						self.client_socket.send('HTTP/1.1 200 OK\r\n\r\n'+get_file('gambar1.jpg'))
						#self.client_socket.send('HTTP/1.1 200 OK\r\n\r\ntes')
					elif arraymessage[1]=="/gambar2":
						self.client_socket.send('HTTP/1.1 200 OK\r\n\r\n'+get_file('gambar2.jpg'))
						#self.client_socket.send('HTTP/1.1 200 OK\r\n\r\ntes')
					elif arraymessage[1]=="/gambar3":
						self.client_socket.send('HTTP/1.1 200 OK\r\n\r\n'+get_file('gambar3.jpg'))
						#self.client_socket.send('HTTP/1.1 200 OK\r\n\r\ntes')
					elif arraymessage[1]=="/gambar4":
						self.client_socket.send('HTTP/1.1 200 OK\r\n\r\n'+get_file('gambar4.jpg'))
						#self.client_socket.send('HTTP/1.1 200 OK\r\n\r\ntes')
					elif arraymessage[1]=="/gambar5":
						self.client_socket.send('HTTP/1.1 200 OK\r\n\r\n'+get_file('gambar5.jpg'))
						#self.client_socket.send('HTTP/1.1 200 OK\r\n\r\ntes')
					elif arraymessage[1]=="/gambar6":
						self.client_socket.send('HTTP/1.1 200 OK\r\n\r\n'+get_file('gambar6.jpg'))
						#self.client_socket.send('HTTP/1.1 200 OK\r\n\r\ntes')
					elif arraymessage[1]=="/gambar7":
						self.client_socket.send('HTTP/1.1 200 OK\r\n\r\n'+get_file('gambar7.jpg'))
						#self.client_socket.send('HTTP/1.1 200 OK\r\n\r\ntes')
					elif arraymessage[1]=="/gambar8":
						self.client_socket.send('HTTP/1.1 200 OK\r\n\r\n'+get_file('gambar8.jpg'))
						#self.client_socket.send('HTTP/1.1 200 OK\r\n\r\ntes')
					elif arraymessage[1]=="/gambar9":
						self.client_socket.send('HTTP/1.1 200 OK\r\n\r\n'+get_file('gambar9.jpg'))
						#self.client_socket.send('HTTP/1.1 200 OK\r\n\r\ntes')
					elif arraymessage[1]=="/gambar10":
						self.client_socket.send('HTTP/1.1 200 OK\r\n\r\n'+get_file('gambar10.jpg'))
						#self.client_socket.send('HTTP/1.1 200 OK\r\n\r\ntes')
					else:
						#print 'Client finish'
						#self.client_socket.send('HTTP/1.1 200 OK\r\n\r\n'+get_file('gambar.jpg'))
						self.client_socket.send('HTTP/1.1 200 OK\r\n\r\nMASUKKAN NOMOR GAMBAR')
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
