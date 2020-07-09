import os
import shutil

# shutil.copy(os.getcwd()+os.sep+'Módulo 4'+os.sep +
#             'arquivos.txt', os.getcwd()+os.sep+'Copia')

# shutil.copytree(os.getcwd()+os.sep+'Módulo 4'+os.sep + 'desafios texto',
#                 os.getcwd()+os.sep+'Módulo 4'+os.sep+'Copia_diretorio')

# shutil.move(os.getcwd()+os.sep+'Módulo 4'+os.sep +
#             'arquivos.txt', os.getcwd()+os.sep+'Módulo 4' + os.sep + 'Fotos')

# shutil.rmtree(os.getcwd()+os.sep+'Módulo 4'+os.sep + 'Copia_diretorio')

# shutil.make_archive('bacon', 'zip', os.getcwd()+os.sep+'Módulo 4')

# shutil.unpack_archive('bacon.zip', 'bacon')


#Desafio 1
shutil.copy(os.getcwd()+os.sep+'Módulo 4'+os.sep+'nomes.txt',
            os.getcwd()+os.sep+'Módulo 4'+os.sep+'Arquivos 2010'+os.sep)
#Desafio 2
shutil.move(os.getcwd()+os.sep+'Módulo 4'+os.sep+'inscrições.pdf',
            os.getcwd()+os.sep+'Módulo 4'+os.sep+'Documentação'+os.sep)
#Desafio 3
shutil.copytree(os.getcwd()+os.sep+'Módulo 4'+os.sep+'Arquivos 2010',
                os.getcwd()+os.sep+'Módulo 4'+os.sep+'Backup Arquivos 2010')
#Desafio 4
shutil.make_archive(os.getcwd()+os.sep+'Módulo 4'+os.sep+'Documentação',
                    'zip', os.getcwd()+os.sep+'Módulo 4'+os.sep+'Documentação')
#Desafio 5
shutil.move(os.getcwd()+os.sep+'Módulo 4'+os.sep +
            'Documentação.zip', os.getcwd()+os.sep+'Módulo 4'+os.sep+'Backup')
#Desafio 6
shutil.rmtree(os.getcwd()+os.sep+'Módulo 4'+os.sep+'Arquivos 2010')
shutil.rmtree(os.getcwd()+os.sep+'Módulo 4'+os.sep+'Documentação')
#Desafio 7
shutil.make_archive(os.getcwd()+os.sep+'Módulo 4'+os.sep+'Backup Arquivos Python', 'zip',
                    os.getcwd()+os.sep+'Módulo 4'+os.sep)
