import os

what = os.environ['OS']

if what[0:6] == "Window":
    print("windows")
    #windows shell 파일 실행
else:
    #!/bin/bash
    print("linux")
    #리눅스 쉘파ㅓ일 실행
