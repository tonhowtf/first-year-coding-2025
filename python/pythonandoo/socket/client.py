import socket


HOST = 'localhost'
PORT = 8003

arquivo = open('articmacaco.jpg', 'rb')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

message = input("Digite o nome do arquivo: ")
sock.send(message.encode())
sock.send(arquivo.read())

confirmacao = sock.recv(1024)
if confirmacao == b'ok':
    print('Mensagem recebida')