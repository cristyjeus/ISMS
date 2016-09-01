import socket
import threading

HOST = '1.209.148.160'
PORT = 12000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

def sendingMsg():
	while True:
		data = input()
		data = data.encode("utf-8")
		conn.send(data)
	conn.close()

def gettingMsg():
	while True:
		data = conn.recv(1024)
		if not data:
			break
		else:
			data = data.decode("utf-8","ignore")
			print(data)
	conn.close()

threading._start_new_thread(sendingMsg,())
threading._start_new_thread(gettingMsg,())

while True:
	pass
