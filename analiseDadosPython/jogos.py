
import requests


def meu_switch():

    validacao = True

    while validacao :
        z = int(input("Menu : "
                      "\n 1 : Lista"
                      "\n 2 : Vendas Mundiais "
                      "\n 3 : Publicacao Japao "
                      "\n 4 : Vendas Japao "
                      "\n 5 : Sair \n"))
        if z == 1 :
            lista()
        elif z == 2 :
            vendas_mundiais()
        elif z == 3 :
            publicacoes_japao()
        elif z == 4 :
            vendas_japao()
        elif z ==  5 :
            print("Programa encerrado")
            break
        else:
            print("opcao inválida")

url ='https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv'

#Caso a pagina nao esteja fora tratamento de erro
req = requests.get(url, timeout = 5)
if req.status_code != 200:
  print(f"Código de erro {req.status_code}")
  req.raise_for_status()
else:
  print("Conexão efetuada com sucesso!")


csv = requests.get(url).text
csv = csv.splitlines()  # idêntico a csv.split('\n')
rotulos = csv[0].split(',') # quebra a linha no cabecalho
dados = csv[1:]
# Coleta pelo indice a coluna toda, usando o index()
indice_genero = rotulos.index('Genre')
indice_jp = float(rotulos.index('JP_Sales'))
indice_marca = rotulos.index('Publisher')
indice_vendas = float(rotulos.index('Global_Sales'))
generos = ['Action', 'Platform', 'Shooter']

marcas = {}
vendasm = {}
vendasj = {}
vendasp = {}
vendass = {}

def lista():
#Quais são as três marcas que mais publicaram jogos dos três gêneros combinados? Indique também o total de jogos de cada marca.
    for elemento in dados:
        elemento = elemento.split(',')
        if elemento[indice_genero] in generos:
            # Coloco indice_marca(index) dentro de uma variavel e depois uso ela como indice para percorrer o dicionario
            marca = elemento[indice_marca]
            #Percorro o dicionario e pergunto voce ja tem essa marca ai, se nao ele coloca, muito bom para nao repetir a marca
            if marca not in marcas:
                # marcas é um dicionario, ele foi povoado por marca agora ele recebe mais atributos, publicacao e vendas mundiais...
                # A linha abaixo vai incrementando valores aos elementos
                marcas[marca] = {'Publicacoes': 0, 'Vendas_Mundiais': 0.0, 'Publicacoes_jp': 0, 'Vendas_jp': 0.0}

            marcas[marca]['Publicacoes'] += 1
            marcas[marca]['Vendas_Mundiais'] += float(rotulos.index('Global_Sales'))
            marcas[marca]['Publicacoes_jp'] += float(rotulos.index('Other_Sales'))
            marcas[marca]['Vendas_jp'] += float(rotulos.index('JP_Sales'))

    # Funcao que inverte usando uma chave, no caso usei lambda
    for espaco in (sorted(marcas.items(), key=lambda item: item[1]['Publicacoes'], reverse=True)):
        print(espaco)

def vendas_mundiais():
#Quais são as três marcas que mais venderam os três gêneros combinados? Indique também o total de vendas de cada marca.
    for elemento in dados:
        elemento = elemento.split(',')
        if elemento[indice_genero] in generos:
            marca = elemento[indice_marca]
            if marca not in vendasm:
                vendasm[marca] = {'Publicacoes': 0, 'Vendas_Mundiais': 0.0}

            vendasm[marca]['Publicacoes'] += 1
            vendasm[marca]['Vendas_Mundiais'] += float(rotulos.index('Global_Sales'))

    # Funcao que inverte usando um indice e um parametro
    for espaco in (sorted(vendasm.items(), key=lambda item: item[1]['Publicacoes'], reverse=True)):
        print(espaco)

def publicacoes_japao():
#Qual foi a marca que mais publicacao em cada um desses gêneros nos últimos dez anos, no Japão? Indique também o total de vendas dela.la.
    total_action = 0
    total_platform = 0
    total_shooter = 0
    empresa_a = []
    empresa_b = []
    empresa_c = []

    for elemento in dados:
        elemento = elemento.split(',')
        if elemento[3] in generos and elemento[7] != '0.0' and elemento[7] != 'N/A' :
            if elemento[indice_genero] == 'Action':
                empresa_a.append(elemento[indice_marca])
                #Usei isso para percorrer dentro dela mesmo quantas vezes o nome da mesma empresa aparece, faco essa operacao dentro do dicionario
                contagemAction = {p: empresa_a.count(p) for p in empresa_a if p in empresa_a}
                #Incrementando os jogos
                total_action = total_action + 1

            if elemento[3] == 'Platform':
                empresa_b.append(elemento[indice_marca])
                total_platform = total_platform + 1
                contagemPlatform = {p:  empresa_b.count(p) for p in  empresa_b if p in  empresa_b}

            if elemento[3] == 'Shooter':
                empresa_c.append(elemento[indice_marca])
                total_shooter = total_shooter + 1
                contagemShooter = {p: empresa_c.count(p) for p in empresa_c if p in empresa_c}

    #Junto genero e o total de jogos de cada genero
    total = [total_action, total_platform, total_shooter]
    text = ''
    for n, a in zip(generos, total):
        text += '\n Genero no Japao {}  {} vendas'.format(n, a)

    print(text)
    # imprimo a contagem por de cada marca por genero
    print('Empresas com mais publicacao no genero ação Japão' + " " + str(contagemAction))
    print('Empresas com mais publicacao no genero platform no Japão' + " " + str(contagemPlatform))
    print('Empresas com mais publicacao no genero Shooter Japão' + " " + str(contagemShooter))

def vendas_japao() :
# Qual é a marca com mais vendas em cada um dos gêneros nos últimos dez anos no Japão? Indique também o número total de jogos dela.

    for elemento in dados:
        elemento = elemento.split(',')
        if elemento[7] != '0.0' and elemento[7] != 'N/A' and elemento[indice_genero] in generos :
            # Coloco indice_marca(index) dentro de uma variavel e depois uso ela como indice para percorrer a o dicionario
            marca = elemento[indice_marca]
            if elemento[indice_genero] == 'Action':
                # Dicionario usado para colocar as marcas, publicacao e vendas, uso o indice marca para checar se existe ja aquele elemento na lista
                if marca not in vendasj:
                    vendasj[marca] = {'Publicacoes': 0, 'Vendas_Japao': 0.0}
                    # vendasj é um dicionario, ele foi povoado por marca agora ele recebe mais atributos, publicacao e vendas de jogo
                    #A linha abaixo vai incrementando valores aos elementos
                vendasj[marca]['Publicacoes'] += 1
                vendasj[marca]['Vendas_Japao'] += float(rotulos.index('JP_Sales'))
            # Foi o jeito que encontrei para selecionar o genero, nao foi muito bonito mais funcionou
            if elemento[indice_genero] == 'Platform':
                plataforma = elemento[indice_marca]
                if plataforma not in vendasp:
                    vendasp[plataforma] = {'Publicacoes': 0, 'Vendas_Japao': 0.0}
                vendasp[plataforma]['Publicacoes'] += 1
                vendasp[plataforma]['Vendas_Japao'] += float(rotulos.index('JP_Sales'))

            if elemento[indice_genero] == 'Shooter':
                shooter = elemento[indice_marca]
                if shooter not in vendass:
                    vendass[shooter] = {'Publicacoes': 0, 'Vendas_Japao': 0.0}
                vendass[shooter]['Publicacoes'] += 1
                vendass[shooter]['Vendas_Japao'] += float(rotulos.index('JP_Sales'))

    # Funcao que inverte usando um indice e um parametro
    print("Action")
    for espaco in (sorted(vendasj.items(), key=lambda item: item[1]['Vendas_Japao'], reverse=True)):
        print(espaco)

    print("Platform")
    for espaco in (sorted(vendasp.items(), key=lambda item: item[1]['Vendas_Japao'], reverse=True)):
        print(espaco)

    print("Shooter")
    for espaco in (sorted(vendass.items(), key=lambda item: item[1]['Vendas_Japao'], reverse=True)):
        print(espaco)


if __name__ == "__main__":
    print (meu_switch())