import socket 
import threading
import errno
import os

host = "1.209.148.159"
port = 8050

global users
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
users=[]

# def serv(c):
#     try:
#         name=c.recv(1024)
#
#         name = name.decode("utf-8","ignore")
#
#         str='[ '+name+' has entered ]'
#         while c:
#             print(str)
#             try:
#                 data = c.recv(1024)
#                 data = data.decode("utf-8","ignore")
#                 str='['+name+'] : ' + data
#                 for each in users:
#                     if c != each:
#                         each.send(str.encode("utf-8"))
#             except socket.error as error:
#                 if error.errno == errno.WSAECONNRESET:
#                     users.remove(e)
#
#     except Exception as e:
#         print(e)
#         users.remove(c)
#         str='[ '+name+'has exited ]'
#         print(str)
#         if users:
#             for each in users:
#                 each.send(str)

def serv(c):
    while 1:

        try:
            name=c.recv(1024)

            name = name.decode("utf-8","ignore")

            str='[ '+name+' has entered ]'
            while c:
                print(str)
                data = c.recv(1024)
                data = data.decode("utf-8", "ignore")
                if data == "ready":
                    str = "go"
                    c.send(str.encode("utf-8"))
                    with open ('test.exe','rb') as script:
                        fileSize = script.seek(0,2)
                        count = int(fileSize / 1024)
                        script.seek(0)
                        if 0 < fileSize%1024:
                            count = count + 1
                        print(count)
                        for i in range(count):
                            #c.send(str.encode("utf-8"))
                            print("send : ",i)
                            c.send(script.read(1024))
                        str = "end"
                        c.send(bytes(str,"UTF-8"))
                else:
                    str = '['+name+'] : ' + data
                    for each in users:
                        if c != each:
                            each.send(str.encode("utf-8"))
                if data == "q":
                    users.remove(c)
                    break


        # except Exception as e:
        #     print(e)
        #     users.remove(c)
        #     str='[ '+name+'has exited ]'
        #     print(str)
        #     if users:
        #         for each in users:
        #             each.send(str)
        except socket.error as error:
            print(error)
            if error.errno == errno.WSAECONNRESET:
                users.remove(c)
                print("exit")
                break

def sendMsg(c):
    while True:
        data = input()
        data = data.encode("utf-8")
        print(users)
        for each in users:
            each.send(data)


while 1:
    c,addr=s.accept()
    users.append(c)
    print(users)
    threading._start_new_thread(serv,(c,))
    threading._start_new_thread(sendMsg, (c,))
