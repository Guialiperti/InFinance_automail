import smtplib
import csv
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

#Número da coluna com o nome
n_nome = 1
#Número da coluna com o e-mail
n_email = 2
#Nome do Excell em .csv (Precisa estar entre aspas)
nome_excel = 'eventos.csv'
#Assunto do e-mail
subject = 'Evento InFinance'
#Assinatura no fim do e-mail
assinatura = 'João Morales' + '\nGerente de Eventos | InFinance \n guilhermeda2@al.insper.edu.br \nRua Quatá, 300 - São Paulo/SP | www.infinanceinsper.com'
imagem = 'logo.png'
#Usuário do e-mail
email_user = 'eventosinfinance@gmail.com'
#Mensagem do e-mail
body = "Esse eh um email teste de imagem"

#-------------------------------------------------
email_send = ''
email_password = input('Senha:') 
fp = open(imagem, 'rb')
# Create a MIMEImage object with the above file object.
msgImage = MIMEImage(fp.read())
# Do not forget close the file object after using it.
fp.close()

with open(nome_excel) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    lista_dicionario = []
    for row in readCSV:
        dict_atual = {}
        dict_atual["nome"] = row[n_nome - 1]
        dict_atual["email"] = row[n_email - 1]
        lista_dicionario.append(dict_atual)
lista_dicionario.pop(0)

for indice in range(len(lista_dicionario)):
    email_send = lista_dicionario[indice]["email"]
    msg = MIMEMultipart() #chamando a biblioteca
    msg['From'] = email_user #email "de"
    msg['To'] = email_send #email "para"
    msg['Subject'] = subject #assunto do emails
    msg.attach(MIMEText(body,'plain')) #juntando corpo
    part = MIMEBase('application','octet-stream')
    msgText = MIMEText('<b>This is the <i>HTML</i> content of this email</b> it contains an image.<br><img src="cid:image1"><br>', 'html')
    msg.attach(msgText)
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)
    #image = MIMEImage(img_data, name= "logo")
    #msg.attach(image)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587) #server do gmail
    server.starttls()
    server.login(email_user,email_password) #fazendo login

    server.sendmail(email_user,email_send,text) #e enviando


server.quit() #saindo do servidor