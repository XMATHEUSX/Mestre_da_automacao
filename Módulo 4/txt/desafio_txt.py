import os

frutas = ['Maçã', 'Banana', 'Uva', 'Laranja', 'Limão']
cores = ['Azul', 'Amarelo', 'Roxo', 'Verde', 'Vermelho']
ling_prog = ['Python', 'Php', 'Java', 'C++', 'C#']
arqs = ['senhas.pdf', 'text.docx', 'cpfs.xlsx']

# Desafio 1
with open('Módulo 4'+os.sep+'txt'+os.sep+'frutas.txt', 'w', encoding="utf8") as arquivos:
    for fruta in frutas:
        arquivos.write(str(fruta)+'\n')

# Desafio 2
with open('Módulo 4'+os.sep+'txt'+os.sep+'frutas.txt', 'r', encoding="utf8") as arquivos:
    for fruta in frutas:
        print(arquivos.read())

# Desafio 3
with open('Módulo 4'+os.sep+'txt'+os.sep+'frutas.txt', 'a', encoding="utf8") as arquivos:
    for cor in cores:
        arquivos.write(str(cor)+'\n')
# desafio 4
with open('Módulo 4'+os.sep+'txt'+os.sep+'Top 5 Linguagens.txt', 'w', encoding="utf8") as arquivos:
    for Linguagem in ling_prog:
        arquivos.write(str(Linguagem)+'\n')
# bônus
for arq in arqs:
    with open(arq, 'w', encoding="utf8") as arquivos:
        pass
