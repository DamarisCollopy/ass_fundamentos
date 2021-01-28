import pandas as pd
import requests
from matplotlib import pyplot as plt

url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv'

#Caso a pagina nao esteja fora tratamento de erro
req = requests.get(url, timeout = 5)
if req.status_code != 200:
  print(f"Código de erro {req.status_code}")
  req.raise_for_status()
else:
  print("Conexão efetuada com sucesso!")

# Lendo csc com pandas
readThis = pd.read_csv(url,  sep=',\s+', delimiter=',', encoding="utf-8", skipinitialspace=True)

# Lista usada para selecao
esporte_selecionado = ['Skating', 'Ice Hockey', 'Skiing', 'Curling']
paises = ['SWE', 'NOR', 'DEN']
medalhas = ['Gold','Silver','Bronze']
#Dicionarios gerados para armazenar dados
dic_medalhas = {}
tabela = {}

def meu_switch():
    validacao = True

    while validacao:
        z = int(input("Menu : "
                      "\n 1 : Paises com mais medalhas "
                      "\n 2 : Sair \n"))
        if z == 1:
            relatorio()
        elif z == 2:
            print("Programa encerrado")
            break
        else:
            print("opcao inválida")

def relatorio() :
    #print(readThis.head(10))
    #print(readThis.groupby('NOC').Sport.first())
    medalhas_ranking = readThis.NOC.value_counts()
    # usar o dataframe para arrumar o codigo para a presentacao renomeando colunas e gerando uma visualizacao mais limpa
    medalhas_ranking = pd.DataFrame(medalhas_ranking)
    # Renomei a coluna
    medalhas_ranking.columns = ['Ranking de Medalhas']
    # Gerei um nome para a coluna
    medalhas_ranking.columns.name = 'Paises'
    print(medalhas_ranking)

    # matplotlib para plotar um grafico
    plt.title('Ranking de Medalhas')
    # grafico legenda
    plt.ylabel("Paises", fontsize=16)
    plt.xlabel("Numero de Medalhas", fontsize=16)
    plt.plot(medalhas_ranking.head(10))
    plt.show()

if __name__ == "__main__":
    print(meu_switch())