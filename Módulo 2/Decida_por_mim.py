import time
import random


def Pensando(tempo):
    print("\rPensando{}".format(
        '.' * int(tempo * 1)), end='')


resposta = ["Não Sei", "com certeza", "Melhor não", "Siga Seu coração",
            "Melhor Pensar em outra coisa", "Não", "Sim", "Vai Estudar", "Existem coisa melhores", "Claro"]

while True:
    Pergunta = input("Qual a sua Dúvida ? ")
    for i in range(1, 4):
        Pensando(i)
        time.sleep(1)
    print("\n"+random.choice(resposta))
    while True:
        continuar = input("Você possui mais dúvidas ? (S/N)")
        if continuar == "N" or continuar == "n":
            break
        elif continuar == "S" or continuar == "s":
            break
        else:
            print("Entrada  incorreta")
    if continuar == "N" or continuar == "n":
        break
print("Obrigado Por Usar O Programa")
