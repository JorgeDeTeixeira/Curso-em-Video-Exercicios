# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

# 0 – 1 – 1 – 2 – 3 – 5 – 8
n = int(input("Quantos termos você quer mostrar?"))
primeiro = 0
segundo = 1
terceiro = primeiro + segundo
cont = 2
print("0 -> 1", end=' -> ')
while cont < n:
    print(f"{terceiro}", end=' -> ')
    primeiro = segundo
    segundo = terceiro
    terceiro = primeiro + segundo
    cont += 1
print("FIM")