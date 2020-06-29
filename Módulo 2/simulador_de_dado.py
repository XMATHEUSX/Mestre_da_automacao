import random


class dado:
    def __init__(self, lados):
        self.lados = lados

    def jogar_dados(self):
        while True:
            print(random.randrange(1, (self.lados)+1))
            while True:
                continuar = input("Continuar jogando ? (S/N)")
                if continuar == "N" or continuar == "n":
                    break
                elif continuar == "S" or continuar == "s":
                    break
                else:
                    print("***Entrada  incorreta***\n ")
            if continuar == "N" or continuar == "n":
                break
        print("os dados foram deixados de lado")


dado_20 = dado(20)
dado_20.jogar_dados()
