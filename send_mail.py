import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

with open('Processo_Seletivo_2018_2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    lista_nomes = []
    lista_emails = []
    lista_datas_preferencia = []
    for row in readCSV:
        nome = row[1]
        email = row[2]
        data_preferencia = row[6]
        lista_nomes.append(nome)
        lista_emails.append(email)
        lista_datas_preferencia.append(data_preferencia)
    lista_nomes.pop(0)
    lista_emails.pop(0)
    lista_datas_preferencia.pop(0)

email_user = 'infinanceinsper@gmail.com' #email do GreenInsper
email_password = '' #senha
email_send = ' ' #variavel aberta pra enviar o email

subject = 'Processo seletivo InFinance' #assunto do email

for indice in range(len(lista_nomes)):	
	email_send = lista_emails[indice] #definindo o destinatário como esse email
	msg = MIMEMultipart() #chamando a biblioteca
	msg['From'] = email_user #email "de"
	msg['To'] = email_send #email "para"
	msg['Subject'] = subject #assunto do emails
	#corpo de texto
	body = 'Boa noite, {0}\nSua inscrição para a 1ª fase do Processo Seletivo do InFinance foi confirmada! A data que você escolheu para a realização da prova foi {1}. Lembre-se de que a prova começará às 18h e acontecerá na sala Jorge Paulo Lemann – primeiro andar. \nPrograme-se para não se atrasar! \nA 1ª fase do nosso Processo Seletivo consiste em uma prova de múltipla escolha que contém 15 questões de matemática lógica e 15 questões de atualidades. Você terá 1h para a realização dos testes. O uso de calculadora científica será permitido. \nBoa sorte, \nDrusco o chefao do ps'.format(
		lista_nomes[indice], lista_datas_preferencia[indice])
	msg.attach(MIMEText(body,'plain')) #juntando corpo

	part = MIMEBase('application','octet-stream')
	part.add_header('Content-Disposition',"attachment; filename= ")

	text = msg.as_string()
	server = smtplib.SMTP('smtp.gmail.com', 587) #server do gmail
	server.starttls()
	server.login(email_user,email_password) #fazendo login

	server.sendmail(email_user,email_send,text) #e enviando

server.quit() #saindo do servidor