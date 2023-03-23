import os

if os.path.exists("./SO/pastamyfile/myfile.py") is True:
    os.rename("./SO/pastamyfile/myfile.py", "./SO/pastamyfile/myfile.txt")
else:
    os.rename("./SO/pastamyfile/myfile.txt", "./SO/pastamyfile/myfile.py")
