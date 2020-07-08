import os
import shutil

shutil.copy(os.getcwd()+os.sep+'bacon.txt',os.getcwd()+os.sep+'Copia')
shutil.copytree(os.getcwd()+os.sep+'desafios texto',os.getcwd()+os.sep+'Copia')
shutil.move(os.getcwd()+os.sep+'bacon.txt', os.getcwd()+os.sep+'Fotos')
shutil.rmtree(os.getcwd()+os.sep+'Copia')
shutil.make_archive('bacon','zip',os.getcwd()+os.sep)
shutil.unpack_archive('bacon.zip','bacon')


# Desafio 1
shutil.copy(os.getcwd()+os.sep+'nomes.txt',os.getcwd()+os.sep+'Arquivos 2010')
# Desafio 2
shutil.move(os.getcwd()+os.sep+'inscrições.pdf',os.getcwd()+os.sep+'Documentação')
# Desafio 3
shutil.copytree(os.getcwd()+os.sep+'Arquivos 2010',
                os.getcwd()+os.sep+'Backup Arquivos 2010')
# Desafio 4
shutil.make_archive('Documentação', 'zip', os.getcwd()+os.sep+'Documentação')
# Desafio 5
shutil.move(os.getcwd()+os.sep+'Documentação.zip',os.getcwd()+os.sep+'Backup')
# Desafio 6
shutil.rmtree(os.getcwd()+os.sep+'Arquivos 2010')
shutil.rmtree(os.getcwd()+os.sep+'Documentação')
# Desafio 7
shutil.make_archive('Backup Arquivos Python','zip',os.getcwd()+os.sep)
