# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Digite o sei sálario R$:"))
if salario < 1250:
    aum = 15
    aumento = salario + (salario / 100 * 15)
else:
    aum = 10
    aumento = salario + (salario / 100 * 10)
print(f"Você teve um aumento de {aum}%, seu novo sálario é de R${aumento:.2f} reais.")