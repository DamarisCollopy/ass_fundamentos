#Escreva uma função em Python que leia uma tupla contendo números inteiros, retorne uma lista contendo somente os números
# ímpares e uma nova tupla contendo somente os elementos nas posições pares.

lista = []
lista_par = []

def par():

    tupla = (1,2,3,4,5,6,7,8,9,10)

    for i in range(len(tupla)) :
        if i % 2 == 0:
            lista_par.append(i)
            tuple(lista_par)
    print(lista_par)

def impar(lista_par) :

    for x in range(len(lista_par)):
        if x % 2 != 0 :
            lista.append(x)

    print(tuple(lista))

par()
impar(lista_par)



