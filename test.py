import os
from subprocess import Popen
what = os.environ['OS']

if what[0:6] == "Window":
    p = Popen("test.bat",cwd=r"./")

    stdout, stderr = p.communicate()
    try:
        os.remove("./test.bat")
    except Exception as e:
        print("except",e)
    #windows shell 파일 실행
else:
    #!/bin/bash
    print("linux")
    #리눅스 쉘파ㅓ일 실행





#  파일 확장자 찾아서 삭제
# # -*- coding: cp949-*-
# import os, sys
#
# def findNremove(path,pattern,maxdepth=1):
#     cpath=path.count(os.sep)
#     for r,d,f in os.walk(path):
#         if r.count(os.sep) - cpath < maxdepth:
#             for files in f:
#                 if files.endswith(pattern):
#                     try:
#                         print("Removing %s" % (os.path.join(r,files)))
#                         print("filename : %s" % files)
#                         os.remove("./%s"%files)
#                         #os.remove(os.path.join(r,files))
#                     except Exception as e:
#                         print (e)
#                     else:
#                         print ("%s removed" % (os.path.join(r,files)))
#
# if __name__ == '__main__':
#     findNremove("C:/Users/cristyjeus/Documents/GitHub/ISMS",".bat",2)
