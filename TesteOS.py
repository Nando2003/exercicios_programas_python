strg = "Fernando"

with open("./SO/pastamyfile/text.txt", 'w') as f:
    # print(f)
    print(f.writable())
    f.write(strg)

with open("./SO/pastamyfile/text.txt", 'a') as f:
    f.write(" Fontes")
