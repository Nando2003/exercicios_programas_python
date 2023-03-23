import smtplib

conexao = smtplib.SMTP('smtp-mail.outlook.com', 587)

conexao.ehlo()
conexao.starttls()
conexao.login('email@outlook.com', 'coxinha123')

lista = ['email2@outlook.com']

for x in lista:
    conexao.sendmail('email@outlook.com', x,
                     'Subject: Nando \n\n Ola amigos sou eu Nando')

conexao.quit()
