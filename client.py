import socket
import threading

HOST = '1.209.148.160'
PORT = 12000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def sendingMsg():
	while True:
		data = input()
		data = bytes(data, "utf-8")
		s.send(data)
	s.close()

def gettingMsg():
	while True:
		data = s.recv(1024)
		data = data.decode("utf-8","ignore")
		print(data)
	s.close()

threading._start_new_thread(sendingMsg,())
threading._start_new_thread(gettingMsg,())

while True:
	pass
