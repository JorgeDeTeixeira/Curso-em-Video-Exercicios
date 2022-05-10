# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
n1 = int(input("Digite o 1° número:"))
n2 = int(input("Digite o 2° número:"))
if n1  > n2:
    print(f"{n1} é maior quê {n2}!")
elif n2 > n1:
    print(f"{n2} é maior quê {n1}!")
else:
    print("Os dois são iguais!")