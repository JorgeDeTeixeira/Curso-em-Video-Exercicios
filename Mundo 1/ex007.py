#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input("Digite a 1° nota:"))
n2 = float(input("Digite a 2° nota:"))
media = (n1 + n2) / 2
print(f"Notas: {n1} e {n2}")
print(f"Média:{media}")