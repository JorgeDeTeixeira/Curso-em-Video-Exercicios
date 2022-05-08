# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
ca = float(input("Cateto adjacente:"))
co = float(input("Cateto oposto:"))
hi = hypot(ca, co)
print(f"Hipotenusa:{hi:.2f}")