# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
atual = date.today().year
ano = int(input("Digite o ano e verifique se ele é bissexto:"))
if ano % 4 == 0 and ano % 100 != 00 or ano % 400 == 0:
    print(f"{ano} é bissexto!")
if ano == 0:
    atual % 4 == 0 and atual % 100 != 00 or atual % 400 == 0
    print(f"{atual} é bissexto!")
else:
    print("Ele não é bissexto!")