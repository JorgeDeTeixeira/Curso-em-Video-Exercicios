# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
preco = float(input("Valor da casa:"))
salario = float(input("Sálario do comprador:"))
prestacao = int(input("Quantos anos de financiamento:"))
mensalidade = preco / (prestacao * 12)
excedente = salario / 100 * 30
print(f"Para pagar uma casa de {preco:.2f} em {prestacao} anos")
print(f"A prestação será de R${mensalidade} reais.")
if mensalidade <= excedente:
    print("Empréstimo pode ser CONCEDIDO")
else:
    print("Empréstimo NEGADO!")