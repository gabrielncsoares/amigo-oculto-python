import random
import smtplib
import email.message

def sortear_elemento(lst):
    if not lst:
        return None
    nome_aleatorio = random.choice(lst)
    return nome_aleatorio

def sorteio(lst):
    random.seed(1)
    sorteios = []
    nomes_disponiveis = list(lst)
    for nome in lst:
        nome_sorteado = sortear_elemento(lst)
        while True:
            nome_sorteado = sortear_elemento(nomes_disponiveis)
            if nome_sorteado != nome and (nome, nome_sorteado) not in sorteios and (nome_sorteado, nome) not in sorteios:
                break
        sorteios.append((nome, nome_sorteado))
        nomes_disponiveis.remove(nome_sorteado)
    return sorteios

def apresentar_sorteados(sorteios):
        sorteio_texto = []
        for tupla in sorteios:
            sorteio_texto.append(f'{tupla[0]} sorteou {tupla[1]}')
        return sorteio_texto

lista = ('Gabriel Soares', 'João Silva', 'Carol Silva', 'Isabela Lage')
tuplas = sorteio(lista)
resultado = apresentar_sorteados(tuplas)
# print(resultado)

gabriel = [valor for valor in resultado if 'Gabriel Soares' in valor and 'sorteou' in valor and valor.index('Gabriel Soares') < valor.index('sorteou')]
joao = {valor for chave, valor in resultado.items() if 'João Silva' in valor and valor.index('João Silva') < valor.index('sorteou')}
carol = {valor for chave, valor in resultado.items() if 'Carol Silva' in valor and valor.index('Carol Silva') < valor.index('sorteou')}
isabela = {valor for chave, valor in resultado.items() if 'Isabela Lage' in valor and valor.index('Isabela Lage') < valor.index('sorteou')}

def enviar_email():  
    corpo_email = f'{list(gabriel)[0].replace('Gabriel Soares', 'Você')}'
    msg = email.message.Message()
    msg['Subject'] = "Sorteio"
    msg['From'] = 'e-mail de origem'
    msg['To'] = 'e-mail de destino'
    password = 'sua senha' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()
