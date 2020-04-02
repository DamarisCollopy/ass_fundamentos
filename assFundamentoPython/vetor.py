# Escreva um programa em Python que leia um vetor de 5 números
# inteiros e o apresente na ordem inversa. Imprima o vetor no final. Use listas.

v = []
nome = []

def vetor(v) :

    for i in range (5) :
        v.append(int(input("Numeros" + str(i +1))))

    v.reverse()
    print(v)

def leia_nome(nome) :

    for i in range (10) :
        print("Escreva letras")
        nome.append(input("Letra : " + str(i + 1)))

    nome.reverse()
    print(nome)

vetor(v)

leia_nome(nome)