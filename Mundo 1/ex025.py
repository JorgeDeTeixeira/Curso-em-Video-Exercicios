# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input("Digite o seu nome:")).strip().upper()
print(f"Seu nome tem Silva? {'SILVA' in nome}")