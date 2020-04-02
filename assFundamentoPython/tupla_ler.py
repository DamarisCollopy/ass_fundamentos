# Usando o Thonny, escreva um programa em Python que
# leia uma tupla contendo 3 números inteiros, (n1, n2, n3) e os imprima em ordem crescente.

print("Insira os numeros:")
n1 = int(input("Numero 1"))
n2 = int(input("Numero 2"))
n3 = int(input("Numero 3"))

tuple = (n1,n2,n3)
print(tuple)
print(sorted(tuple))
