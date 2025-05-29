#Vamos criar uma função que recebe um número e imprime a contagem regressiva até 0
def numero(n):
    if n < 0:  #Caso base
        return      #Acaba o loop infinito já que quando n<0 
    print(n)
    numero(n-1)  #chamada da função com o próximo número dentro da mesma

n = int(input("Enter a random number: "))
numero(n)