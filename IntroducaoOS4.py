import os

if os.path.exists("./SO/pastamyfile/receita.txt") is False:
    f = open('./SO/pastamyfile/receita.txt', 'w')

arquivo = open('./SO/pastamyfile/receita.txt')
# print(arquivo.closed) == FALSE - O arquivo está aberto
# print(arquivo.read())  # quantos bits retorna
print(arquivo.readline())  # lê linha
print(arquivo.readline())
print(arquivo.closed)
arquivo.close()  # fecha o arquivo
print(arquivo.closed)  # == True - O arquivo está fechado
