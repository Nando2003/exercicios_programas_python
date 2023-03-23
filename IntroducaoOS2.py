import os

if os.path.exists("./SO/pastamyfile/text.txt") is False:
    f = open('./SO/pastamyfile/text.txt', 'w')
else:
    # Deletar Arquivo
    os.remove('./SO/pastamyfile/text.txt')

if os.path.exists("./SO/pastamyfile/myfile") is False:
    os.mkdir('./SO/pastamyfile/myfile')
else:
    # Deletar Folder
    os.rmdir('./SO/pastamyfile/myfile')
