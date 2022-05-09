# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input("Digite o 1° valor:"))
b = int(input("Digite o 2° valor:"))
c = int(input("Digite o 3° valor:"))

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f"O maior valor digitado:{maior}")
print(f"O menor valor digitado:{menor}")