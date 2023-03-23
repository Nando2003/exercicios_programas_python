import smtplib

conexao = smtplib.SMTP('smtp-mail.outlook.com', 587)

conexao.ehlo()
conexao.starttls()
conexao.login('nandolff2@outlook.com.br', 'LFhf!@61')

lista = ['nandofontes30@gmail.com']

for x in lista:
    conexao.sendmail('nandolff2@outlook.com.br', x,
                     'Subject: Nando \n\n Ola amigos sou eu Nando')

conexao.quit()
