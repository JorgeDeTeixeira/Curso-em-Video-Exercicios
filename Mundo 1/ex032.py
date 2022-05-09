# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input("Digite o ano e verifique se ele é bissexto:"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 00 or ano % 400 == 0:
    print(f"{ano} é bissexto!")
else:
    print("Ele não é bissexto!")