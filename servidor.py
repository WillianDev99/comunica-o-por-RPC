# coding: utf-8 
from xmlrpc.server import SimpleXMLRPCServer
import random

HOST = '127.0.0.1'
PORT = 50000

def dica_palavra():
    dica = "NOME DE PESSOA."
    return dica

def carrega_palavra_secreta():
    palavras = []
    with open("palavra.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def resultado_jogo(resultado):
    if resultado == 'Acertou':
        print("O cliente acertou a palavra!!!")
        print('Fechando a conexão.')
        return 0
    else:
        print("O cliente errou a palavra!!!")
        print('Fechando a conexão.')
        return 0

servidor = SimpleXMLRPCServer((HOST, PORT))
servidor.register_function(dica_palavra)
servidor.register_function(carrega_palavra_secreta)
servidor.register_function(resultado_jogo)
print('SERVIDOR LIGADO!!!')
servidor.serve_forever()
print('Aguardando conexão de um cliente!!!')
