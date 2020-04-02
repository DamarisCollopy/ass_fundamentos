#Para cada esporte, considere todas as modalidades, tanto o masculino, quanto o feminino,
# e imprima um relatório mostrando o total de medalhas de cada um dos países e em que esporte,
# ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida.

import requests

url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv'

#Caso a pagina nao esteja fora tratamento de erro
req = requests.get(url, timeout = 5)
if req.status_code != 200:
  print(f"Código de erro {req.status_code}")
  req.raise_for_status()
else:
  print("Conexão efetuada com sucesso!")

csv = requests.get(url).text
linhas = csv.splitlines()

esporte_selecionado = ['Skating', 'Ice Hockey', 'Skiing', 'Curling']
paises = ['SWE', 'NOR', 'DEN']
medalhas = ['Gold','Silver','Bronze']

dic_medalhas = {}
tabela = {}

def relatorio() :
    tabela['Gold','Silver','Bronze'] = []

    for linha in linhas:
        colunas = linha.split(',')

        if colunas[7] in medalhas:
            # Uma string na forma: Ano (Cidade) | Esporte | Gênero | Medalha
            tabela['Gold','Silver','Bronze'].append(
                f" País : {colunas[4]:20} Ano : {colunas[0]:20} 'Cidade : {colunas[1]:20}  Esportes : {colunas[2]:20}  Genero : {colunas[6]} Medalhas : {colunas[7]} ")

    for medalha in tabela['Gold','Silver','Bronze']:
        print(medalha)

def exibir_dados(p):
    for linha in linhas:
      colunas = linha.split(',')

      if colunas[4] == p:
        # Uma string na forma: Ano (Cidade) | Esporte | Gênero | Medalha
        dic_medalhas[p].append(f"Pais : {colunas[5]} Ano : {colunas[0]:20} 'Cidade : {colunas[1]:20}  Esportes : {colunas[2]:20}  Genero : {colunas[6]} Medalhas : {colunas[7]} ")

    for medalha in dic_medalhas[p]:
      print(medalha)

def alternativa() :
    while True :
        opcao = int(input("Escolha um pais a ser pesquisado :"
                      "\n 1 : Franca"
                      "\n 2 : USA"
                      "\n 3 : Noruega "
                      "\n 4 : Dinamarca"
                      "\n 5: Suecia"
                      "\n 6 : Suica"
                      "\n 7 : Canada"
                      "\n 8 : Finlandia"
                      "\n 9 : Alemanha"
                      "\n 10 : Australia"
                      "\n 11 : Relatorio"
                      "\n 12 : Sair \n" ))
        if opcao == 1 :
            print("Franca")
            dic_medalhas['FRA'] = []
            p = 'FRA'
            exibir_dados(p)
        elif  opcao == 2 :
            print("USA")
            dic_medalhas['USA'] = []
            p = 'USA'
            exibir_dados(p)
        elif opcao == 3:
            print("NORUEGA")
            dic_medalhas['NOR'] = []
            p = 'NOR'
            exibir_dados(p)
        elif opcao == 4:
            print("DINAMARCA")
            dic_medalhas['DIN'] = []
            p = 'DIN'
            exibir_dados(p)
        elif opcao == 5:
            print("Suécia")
            dic_medalhas['SWE'] = []
            p = 'SWE'
            exibir_dados(p)
        elif opcao == 6:
            print("SUICA")
            dic_medalhas['SUI'] = []
            p = 'SUI'
            exibir_dados(p)
        elif opcao == 7:
            print("CANADA")
            dic_medalhas['CAN'] = []
            p = 'CAN'
            exibir_dados(p)
        elif opcao == 8:
            print("FINLANDIA")
            dic_medalhas['FIN'] = []
            p = 'FIN'
            exibir_dados(p)
        elif opcao == 9:
            print("ALEMANHA")
            dic_medalhas['GER'] = []
            p = 'GER'
            exibir_dados(p)
        elif opcao == 10:
            print("AUSTRALIA")
            dic_medalhas['AUT'] = []
            p = 'AUT'
            exibir_dados(p)
        elif opcao == 11:
            print("Relatorio")
            relatorio()
        elif opcao == 12:
            print("Programa encerrado")
            break
        else:
            print("opcao inválida")

if __name__ == "__main__":
    print (alternativa())

