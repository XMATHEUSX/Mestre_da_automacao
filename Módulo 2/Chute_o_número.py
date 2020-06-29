import random


def rodada(inicio, final):
    numero_gerado = random.randint(inicio, final)
    resposta = tentativa(inicio, final)
    while resposta != numero_gerado:
        if resposta > numero_gerado:
            print("chute um valor menor")
        elif resposta < numero_gerado:
            print("chute um valor maior")
        resposta = tentativa(inicio, final)
    print("você acertou Parabéns!!!!")


def tentativa(inicio, final):
    while True:
        try:
            reposta = int(input(f"Chute um valor entre {inicio} até {final}:"))
            break
        except:
            print("***Entrada  incorreta***")
    return reposta


rodada(1, 10)
