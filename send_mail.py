import smtplib
import csv
import json
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def gera_mensagem(tipo, nome, data):

    assinatura = 'Guilherme Drigo de Almeida' + '\nGerente de Processo Seletivo | InFinance \nCel:(11) 96435-9992 | guilhermeda2@al.insper.edu.br \nRua Quatá, 300 - São Paulo/SP | www.infinanceinsper.com'

    if tipo == 'padrao':
        texto = 'Boa noite, {0}\nSua inscrição para a 1ª fase do Processo Seletivo do InFinance foi confirmada! A data para a realização da prova é {1}. Lembre-se de que a prova começará às 18h e acontecerá no auditório. \nPrograme-se para chegar com 15 minutos de antecedência. \nA 1ª fase do nosso Processo Seletivo consiste em uma prova de múltipla escolha que contém 15 questões de matemática lógica e 15 questões de atualidades. O uso de calculadora científica será permitido. \nBoa sorte, \n\n'.format(
                    nome, data) + assinatura
    elif tipo == 'lotacao':
        texto = 'Boa noite, {0}\nSua inscrição para a 1ª fase do Processo Seletivo do InFinance foi confirmada! A data que você escolheu para a realização da prova já está com lotação máxima, dessa forma você deverá realizar a prova no dia {1}. Lembre-se de que a prova começará às 18h e acontecerá no auditório. \nPrograme-se para chegar com 15 minutos de antecedência. \nA 1ª fase do nosso Processo Seletivo consiste em uma prova de múltipla escolha que contém 15 questões de matemática lógica e 15 questões de atualidades. O uso de calculadora científica será permitido. \nBoa sorte, \n\n'.format(
                    nome, data) + assinatura
    elif tipo == 'max':
        texto = 'Boa noite, {0}\nSua inscrição não pode ser feita por conta de lotação máxima do processo seletivo. Por favor entrar em contato no email: guilhermealmeida@gmail.com'.format(
                    nome)
    return texto

#alocação dos dias
lista_dia1 = []
lista_dia2 = []
max_dia1 = 175
max_dia2 = 175
dia1 = '20/08 (segunda-feira)'
dia2 = '22/08 (quarta-feira)'

#Puxando os dados gravados

with open('emails_enviados.txt') as enviados:  
    emails_enviados = json.load(enviados)

with open('lista_dia1.txt') as india1:  
    lista_dia1 = json.load(india1)

with open('lista_dia2.txt') as india2:  
    lista_dia2 = json.load(india2)

with open('Processo_Seletivo_2018_2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    lista_dicionario = []
    for row in readCSV:
        dict = {}
        dict['nome'] = row[1]
        dict['email'] = row[2]
        dict['data'] = row[6]
        lista_dicionario.append(dict)
    lista_dicionario.pop(0)

email_user = 'infinanceinsper@gmail.com' #email do GreenInsper
email_password = getpass.getpass('Senha')
email_send = ' ' #variavel aberta pra enviar o email

subject = 'Processo seletivo InFinance' #assunto do email


for indice in range(len(lista_dicionario)): 
    if not lista_dicionario[indice]['email'] in emails_enviados:
        if lista_dicionario[indice]['data'] == dia1:
            if len(lista_dia1) < max_dia1:
                lista_dia1.append(lista_dicionario[indice]['nome'])
                emails_enviados.append(lista_dicionario[indice]['email'])
                email_send = lista_dicionario[indice]['email'] #definindo o destinatário como esse email
                msg = MIMEMultipart() #chamando a biblioteca
                msg['From'] = email_user #email "de"
                msg['To'] = email_send #email "para"
                msg['Subject'] = subject #assunto do emails
                #Corpo de texto
                body = gera_mensagem('padrao', lista_dicionario[indice]['nome'], lista_dicionario[indice]['data'])
                msg.attach(MIMEText(body,'plain')) #juntando corpo

                part = MIMEBase('application','octet-stream')
                part.add_header('Content-Disposition',"attachment; filename= ")

                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com', 587) #server do gmail
                server.starttls()
                server.login(email_user,email_password) #fazendo login

                server.sendmail(email_user,email_send,text) #enviando
            elif len(lista_dia2) < max_dia2:
                lista_dia2.append(lista_dicionario[indice]['nome'])
                emails_enviados.append(lista_dicionario[indice]['email'])
                email_send = lista_dicionario[indice]['email'] #definindo o destinatário como esse email
                msg = MIMEMultipart() #chamando a biblioteca
                msg['From'] = email_user #email "de"
                msg['To'] = email_send #email "para"
                msg['Subject'] = subject #assunto do emails
                #Corpo de texto
                body = gera_mensagem('lotacao', lista_dicionario[indice]['nome'], dia2)
                msg.attach(MIMEText(body,'plain')) #juntando corpo

                part = MIMEBase('application','octet-stream')
                part.add_header('Content-Disposition',"attachment; filename= ")

                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com', 587) #server do gmail
                server.starttls()
                server.login(email_user,email_password) #fazendo login

                server.sendmail(email_user,email_send,text) #enviando
            else:
                pass

        elif lista_dicionario[indice]['data'] == dia2:
            if len(lista_dia2) < max_dia2:
                lista_dia2.append(lista_dicionario[indice]['nome'])
                emails_enviados.append(lista_dicionario[indice]['email'])
                email_send = lista_dicionario[indice]['email'] #definindo o destinatário como esse email
                msg = MIMEMultipart() #chamando a biblioteca
                msg['From'] = email_user #email "de"
                msg['To'] = email_send #email "para"
                msg['Subject'] = subject #assunto do emails
                #Corpo de texto
                body = gera_mensagem('padrao', lista_dicionario[indice]['nome'], lista_dicionario[indice]['data'])
                msg.attach(MIMEText(body,'plain')) #juntando corpo

                part = MIMEBase('application','octet-stream')
                part.add_header('Content-Disposition',"attachment; filename= ")

                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com', 587) #server do gmail
                server.starttls()
                server.login(email_user,email_password) #fazendo login

                server.sendmail(email_user,email_send,text) #enviando
            elif len(lista_dia1) < max_dia1:
                lista_dia1.append(lista_dicionario[indice]['nome'])
                emails_enviados.append(lista_dicionario[indice]['email'])
                email_send = lista_dicionario[indice]['email'] #definindo o destinatário como esse email
                msg = MIMEMultipart() #chamando a biblioteca
                msg['From'] = email_user #email "de"
                msg['To'] = email_send #email "para"
                msg['Subject'] = subject #assunto do emails
                #Corpo de texto
                body = gera_mensagem('lotacao', lista_dicionario[indice]['nome'], dia1)
                msg.attach(MIMEText(body,'plain')) #juntando corpo

                part = MIMEBase('application','octet-stream')
                part.add_header('Content-Disposition',"attachment; filename= ")

                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com', 587) #server do gmail
                server.starttls()
                server.login(email_user,email_password) #fazendo login

                server.sendmail(email_user,email_send,text) #enviando
            else:
                pass

#Gravando os dados atualizados
with open('emails_enviados.txt', 'w') as outfile:  
    json.dump(emails_enviados, outfile)

with open('lista_dia1.txt', 'w') as outdia1:  
    json.dump(lista_dia1, outdia1)

with open('lista_dia2.txt', 'w') as outdia2:  
    json.dump(lista_dia2, outdia2)

server.quit() #saindo do servidor