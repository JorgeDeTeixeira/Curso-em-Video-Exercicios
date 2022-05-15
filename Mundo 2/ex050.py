# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(0, 6):
    num = int(input(f"Digite o °{c + 1} número:"))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"A soma entre os {cont} valores pares foi:{soma}")