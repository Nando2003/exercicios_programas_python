import os
import shutil

# Procura se arquivo ou diretorio existe
print(os.path.exists('AprendendoPython/Tuplas/tuplas'))

# Cria arquivos
if os.path.exists('AprendendoPython/SO/myfile.py') is False:
    with open("SO/myfile.py", "w") as f:  # mknod no windows
        # (https://www.pythontutorial.net/python-basics/python-create-text-file/)
        f.write('print("Hello world")')

# Criar diretorio
if os.path.exists("SO/pastamyfile") is False:
    os.mkdir('SO/pastamyfile')

# Mover Files para Folders
shutil.move('SO/myfile.py', 'SO/pastamyfile')
