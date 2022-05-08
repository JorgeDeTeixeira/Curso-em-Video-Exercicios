# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Digite seu sálario R$:"))
novo_salario = salario + (salario / 100 * 15)
print(f"Antigo sálario R$:{salario:.2f} reais.")
print(f"Novo sálario com aumento de 15% R$:{novo_salario:.2f} reais")