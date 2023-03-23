import smtplib
import ssl
import email.message

msg = email.message.Message()
setor = "B"
msg['Subject'] = f"Planejamento Legal: {setor}"
body = """
<p>Olá, equipe do financeiro,</p>
<p>Segue em anexo a planilha com os resultados desse mês</p>
<p>Atenciosamente,</p>
<p>Nando</p>
"""
msg['From'] = 'email@outlook.com'
to = ['email@outlook.com', 'email2@outlook.com']
password = 'coxinha123'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(body)

context = ssl.create_default_context()

with smtplib.SMTP('smtp-mail.outlook.com', 587) as conexao:
    conexao.ehlo()
    conexao.starttls(context=context)
    conexao.login(msg['From'], password)

    for x in to:
        print(x)
        conexao.sendmail(msg['From'], x, msg.as_string().encode('utf-8'))
