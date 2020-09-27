import smtplib
import sys

try:
    # Fazendo login no provedor de e-mail.
    login = str(input('Login: ')).strip()
    senha = str(input('Senha: '))
    print('-=' * 15)

    # Cabeçalho de e-mail.
    de = login
    para = str(input('Para: ')).strip()

    # Você pode inserir mais de um destinatario separando por ";"
    paras = para.split(';')
    assunto = f'{str(input("Adicionar assunto: ")).capitalize().strip()}'
    print('-=' * 15)

    # Formatação do cabelho do e-mail.
    # MIME-version: 1.0 e Content-type: text/html aceita padrão de envio em html.
    msg = f'''From: <{de}>
To: {paras}
MIME-version: 1.0
Content-type: text/html
Subject: {assunto}\n\n'''

    # Escreva o conteúdo da mensagem
    print('Pressione ENTER e depois CTRL+D para finalizar a mensagem.')
    print('Mensagem: \n')
    while True:
        # Recebemos uma linha digitada pelo usuário
        linha = sys.stdin.readline()

        # Se o usuário terminar de preencher o texto e fornecer uma linha vazia
        # podemos encerrar a mensagem
        if not linha: break

        # Adicionamos a variavel msg a linha escrita
        msg += linha

    # Eu escolhi o Hotmail, mas aceita outros tipos de provedores.
    servidor = smtplib.SMTP('smtp-mail.outlook.com', 587)

    # Faz conexão com o provedor de e-mail
    servidor.ehlo()

    # Criptografa a conexão para TLS
    servidor.starttls()

    # Autenticando login e senha
    servidor.login(login, senha)

    # Enviando e-mail
    # encerrando conexão
    servidor.sendmail(de, paras, msg.encode('UTF-8'))
    servidor.quit()
    print('-=' * 15)
    print('E-mail enviado com sucesso.')


# Tratamento de possiveis erros
except smtplib.SMTPConnectError:
    print('Ocorreu um erro durante o estabelecimento de uma conexão com o servidor.')

except smtplib.SMTPHeloError:
    print('O servidor recusou a conexão.')

except smtplib.SMTPAuthenticationError:
    print('Login ou senha fornenida estão INCORRETOS.')

except smtplib.SMTPSenderRefused:
    print(f'O endereço < {de} >foi recusado.')

except smtplib.SMTPServerDisconnected:
    print('O servidor foi desconectado inesperadamente')

except smtplib.SMTPRecipientsRefused:
    print('Todos os destinatários foram recusados. Ninguém recebeu o correio.')

except smtplib.SMTPException:
    print('Nenhum método de autenticação adequado foi encontrado.')


