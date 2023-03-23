"""with open("./SO/pastamyfile/receita.txt", 'w') as arquivo:  # w = write
    arquivo.write("Feio")
    print(arquivo.closed)

print(arquivo.closed)"""

texto = """eu sou lindo
eu sou feio"""
texto2 = 'mas nem tanto'

with open("./SO/pastamyfile/receita.txt", 'a') as arquivo:  # a = append
    arquivo.write(texto)
    arquivo.write(f" {texto2}")
