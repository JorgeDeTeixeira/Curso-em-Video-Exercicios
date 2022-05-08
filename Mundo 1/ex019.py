# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice, choices

n1 = str(input("1° aluno:"))
n2 = str(input("2° aluno:"))
n3 = str(input("3° aluno:"))
n4 = str(input("4° aluno:"))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print(f"O aluno escolhido foi:{escolhido}")