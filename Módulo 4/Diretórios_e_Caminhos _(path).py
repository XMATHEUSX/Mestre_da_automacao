import os


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

# Aula 3 criando_diretorios


os.mkdir('Módulo 4'+os.sep+'Arquivos')

os.makedirs('Módulo 4'+os.sep+'Arquivos'+os.sep+'Arquivos pdf')

os.makedirs('Módulo 4'+os.sep+'Fotos'+os.sep+'Fotos Verão')
