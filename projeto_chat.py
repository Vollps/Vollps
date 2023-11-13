import os

mensagens = []

nome = input("Nome: ")

while True:

    #limpar terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("_________________")

    #obter texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    mensagens.append({
        "nome": nome,
        "texto": texto
    })