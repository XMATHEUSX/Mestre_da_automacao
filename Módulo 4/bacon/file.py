import os
import shutil
'''
# 1 todos os arquivos que estão na pasta
atual = os.getcwd()
desafios = (os.listdir())
for root, dir, files in os.walk(atual):
    for file in files:
        print(os.path.join(file))
# 2 Só lista os arquivos da pasta atual
dir_files = next(os.walk('.'))[1]
list_files = next(os.walk('.'))[2]
for file in list_files:
    print(os.path.join(os.getcwd(), file))
# 3  lista os arquivos das sub-pastas
for dir in dir_files:
    list_files = next(os.walk(f'.\\{dir}'))[2]
    for file in list_files:
        print(os.path.join(os.getcwd(), file))

# 4.1 navegando ate a pasta desafios texto
os.chdir('desafios texto')
# 4.2 navegando de volta pra a pasta desafio arquivos
os.chdir('..')
# 4.3 navegando pra o diretorio pais da pasta arquivos
os.chdir('..')
print(os.getcwd())


# desafio aula 3
os.mkdir('Arquivos')
os.makedirs('Arquivos'+os.sep+'Arquivos pdf')
os.makedirs('Fotos'+os.sep+'Fotos Verão')

#######################################################
frutas = ['Maçã', 'Banana', 'Uva', 'Laranja', 'Limão']
cores = ['Azul', 'Amarelo', 'Roxo', 'Verde', 'Vermelho']
ling_prog = ['Python', 'Php', 'Java', 'C++', 'C#']
arqs = ['senhas.pdf', 'text.docx', 'cpfs.xlsx']

# Desafio 1
with open('frutas.txt', 'w', encoding="utf8") as arquivos:
    for fruta in frutas:
        arquivos.write(str(fruta)+'\n')

# Desafio 2
with open('frutas.txt', 'r', encoding="utf8") as arquivos:
    for fruta in frutas:
        print(arquivos.read())

# Desafio 3
with open('frutas.txt', 'a', encoding="utf8") as arquivos:
    for cor in cores:
        arquivos.write(str(cor)+'\n')
# desafio 4
with open('Top 5 Linguagens.txt', 'w', encoding="utf8") as arquivos:
    for Linguagem in ling_prog:
        arquivos.write(str(Linguagem)+'\n')
# bônus
for arq in arqs:
    with open(arq, 'w', encoding="utf8") as arquivos:
        pass
    '''
#############################################################

# shutil.copy(os.getcwd()+os.sep+'bacon.txt',os.getcwd()+os.sep+'Copia')
#shutil.copytree(os.getcwd()+os.sep+'desafios texto',os.getcwd()+os.sep+'Copia')
#shutil.move(os.getcwd()+os.sep+'bacon.txt', os.getcwd()+os.sep+'Fotos')
#shutil.rmtree(os.getcwd()+os.sep+'Copia')
shutil.make_archive('bacon','zip',os.getcwd()+os.sep)
# shutil.unpack_archive()
