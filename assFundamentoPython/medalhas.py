#Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega, verifique:
# No século XXI (a partir de 2001), qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades:

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
nomes_paises = ['Suécia', 'Dinamarca', 'Noruega']
total_medalhas_suecia = 0
total_medalhas_nor = 0
total_medalhas_den = 0

#Percorre com o for a tabela, linhas edidato para pegar do ponto a ser avaliado, e colunas quebra na virgula a leitura usando o split
for linha in linhas:
  colunas = linha.split(',')
  if colunas[4] in ['SWE', 'NOR', 'DEN'] and colunas[2] in ['Skating', 'Ice Hockey', 'Skiing', 'Curling'] and colunas[-1] == 'Gold' and int(colunas[0]) >= 2001:
    if colunas[4] == 'SWE':
      total_medalhas_suecia = total_medalhas_suecia + 1
    print(colunas[0], colunas[2], colunas[4], colunas[-1])
    if colunas[4] == 'NOR':
        total_medalhas_nor = total_medalhas_nor + 1
    print(colunas[0], colunas[2], colunas[4], colunas[-1])
    if colunas[4] == 'DEN' :
        total_medalhas_den = total_medalhas_den + 1
    print(colunas[0], colunas[2], colunas[4], colunas[-1])

total = [total_medalhas_suecia,total_medalhas_den,total_medalhas_nor]
text = ''
for n, a in zip(nomes_paises,total):
    text += '\nO Nome dos Paises {} medalhas de ouro {}'.format(n, a)

print(text)
maior = max(total)
#Usei o zip para interar, dessa forma que fiz tenho que cuidar para a ordem das listas estejam de forma casada, usei um
# if para comparar usando max ele encontra o numero maior na lista e compara e joga o valor casada usando o zip
textC = ''
for n, a in zip(nomes_paises,total):
    if maior == a :
        textC += '\nO  país com mais ouros, no século XXI, nas categorias listadas, é: {} {} ouros '.format(n, a)

print(textC)
