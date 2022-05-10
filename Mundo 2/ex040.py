# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
n1 = float(input("Digite a 1° nota:"))
n2 = float(input("Digite a 2° nota:"))
media = (n1 + n2) / 2
print(f"Notas: {n1} | {n2}")
print(f"Média: {media}")
if media < 5.0:
    print("REPROVADO!")
elif media >= 5.0 and media <= 6.9:
    print("RECUPERAÇÃO!")
else:
    print("APROVADO!")