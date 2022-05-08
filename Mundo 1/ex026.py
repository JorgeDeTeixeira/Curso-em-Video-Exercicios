# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input("Digite uma frase:")).strip().upper()
print(f"Frase:{frase}")
print(f"A letra A aparece {frase.count('A')} vezes.")
print(f"A letra A aparece na posição {frase.find('A') + 1} pela primeira vez.")
print(f"A letra A aparece na posição {frase.rfind('A') + 1 } pela última vez.")