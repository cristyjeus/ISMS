from distutils.core import setup
import py2exe

setup(
    #console=['selectUrl_gui2.py']
    windows=['selectUrl_gui2.py'],
    options=
    {
        'py2exe':
        {
            'includes':["sip","PyQt4.QtGui"],
            'bundle_files':1,
            'dll_excludes':["MSVCP90.dll"]
        }
    },
    zipfile=None,
)



#pip로 py2exe 설치 후 이런식으로 하면 dist폴더에 exe파일 생성이 되고 나머지 파일들은 같이 포함시켜야 실행됨
#includes 쪽은 gui를 위해 PyQt라이브러리를 가져왔기 때문에 포함시켜줘야댄것.
