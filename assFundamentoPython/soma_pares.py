#Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n,
# inclusive. O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.

n = int(input(" Informe o valor de n:")) # dentro do meu for vai ser a quantidade dentro daquele range vai ter numero par

soma = 0

for x in range(1,n + 1) :

# usei a formula para selecionar apenas o numero par o resto de dois se for 0 ele é par
    if x%2 == 0 :
        soma = soma + x

print( "O resultado da soma de numeros pares é : " + " " + str(soma))





