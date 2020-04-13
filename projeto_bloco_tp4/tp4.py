import stat
import os
import time

caminho_path = r"C:\Users\Damaris-PC"
# esse r junto do caminho é uma formatacao para tornar visivel indeferente como o caminho esta inscrito para a bibloteca, pq na hora da leitura a biblioteca pode nao conseguir visualizar o nome

print("Nome : %s" % caminho_path)

#print o diretorio que estou usando no momento, no caso o do programa
#print(os.getcwd())

# Mostra o conteudo dentro daquele diretorio
conteudo = os.listdir(caminho_path)
print(conteudo)

nome = os.stat(caminho_path)
formatar_hora = time.ctime(nome[stat.ST_MTIME])
formatar_criacao = time.ctime(nome[stat.ST_CTIME])
#O "ctime", conforme relatado pelo sistema operacional. Em alguns sistemas (como Unix), é a hora da última alteração de metadados e,
# em outros (como Windows), é a hora de criação (consulte a documentação da plataforma para obter detalhes).
print("Data da Criação:", formatar_criacao)
# biblioteca os stat.St_MTIME funcao que mostra a ultima modificacao, usando a biblioteca time eu consigo formatar o numero apresentado em hora,dia,ano,dia da semana e mes por isso chamei de formatar a hora
print("Data da modificação :", (formatar_hora))
# ST_SIZE Tamanho em bytes de um arquivo simples
tamanho = nome[stat.ST_SIZE]
print("Tamanho da pasta em bytes :", tamanho)

