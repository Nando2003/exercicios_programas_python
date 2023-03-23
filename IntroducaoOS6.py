import pydf
pdf = pydf.generate_pdf('<h1>ola mundo</h1><p>testando o meu documento</p>  ')
with open('./SO/pastamyfile/test_doc.pdf', 'wb') as arquivo:
    arquivo.write(pdf)
