#Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como argumentos
# dois números inteiros, A e B, e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o resultado da
# operação.Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.
import re

def meu_switch():

    validacao = True
    x = 1
    while validacao :
        z = int(input("Menu : "
                      "\n 0 : Potência elevada a 5"
                      "\n 1 : Calculo de potência "
                      "\n 3 : Sair \n"))
        if z < x :
            potencia_elevada5()
        elif z == x :
            entrada_potencia()
        elif z ==  2:
            print("Programa encerrado")
            break
        else:
            print("opcao inválida")


def potencia_elevada5() :

    while(True) :
        potencia = int(input("Numero a ser elevado a potencia de 5"))
        if potencia <= 0 :
            print("Numero Invalido")
        else :
            a = potencia
            for i in range(1, 5):
                potencia = potencia * a

            print(potencia) # para imprimir apenas o resultado final
        break # para voltar ao menu


def entrada_potencia() :

    while True :
        potencia = int(input("Entre com o numero : "))
        if potencia <= 0 :
            print("Numero Invalido")
        else:
            b = int(input("Entre com o numero a ser elevado a potência :"))
            a = potencia

            for i in range(1, b):
                potencia = potencia * a

            print(potencia) # para imprimir apenas o resultado final
        break # para voltar ao menu

# Main para executar o programa, chama o switch
if __name__ == "__main__":
    print (meu_switch())
