from csv import DictReader, DictWriter
import os


pessoas = [{
    "nome": {"Mark"},
    "idade": {'25', '19', '65'},
    "altura": {'170', '160', '175'}
}]


# para ler arquivos
# with open('csv_exemplo.csv') as arquivo:
#     leitor_csv = DictReader(arquivo)
#     for linha in leitor_csv:
#         print(linha['orderId'] + ' ' + linha['First Name'] )

# Criando csv com dictWriter
# with open('pessoas.csv', 'w', newline='') as arquivo:
#     cabecalho = ['Nome', 'Idade', 'Altura']
#     escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
#     escritor_csv.writeheader()
#     escritor_csv.writerow({
#         'Nome':'Mark',
#         'Idade': '25',
#         'Altura':'170'
#     })
#     escritor_csv.writerow({
#         'Nome':'Carol',
#         'Idade': '19',
#         'Altura':'160'
#     })
#     escritor_csv.writerow({
#         'Nome':'Robert',
#         'Idade': '65',
#         'Altura':'175'
#     })


with open('Módulo 4'+os.sep+'csv'+os.sep+'pessoas.csv', 'r') as arquivo_original:
    leitor_csv_original = DictReader(arquivo_original)
    pessoas = list(leitor_csv_original)
    with open('Módulo 4'+os.sep+'csv'+os.sep+'pessoas2.csv', 'w', newline='') as novo_arquivo:
        cabecalho = ['Nome', 'Idade', 'Altura']
        escritor_csv = DictWriter(novo_arquivo, fieldnames=cabecalho)
        escritor_csv.writeheader()
        for linha in pessoas:
            escritor_csv.writerow({
                'Nome': linha['Nome'],
                'Idade': linha['Idade'],
                'Altura': linha['Altura']+'cm',
            })
