# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input("Digite o preço do produto:"))
novo_preco = preco - (preco / 100 * 5)
print(f"Antigo preço:R${preco:.2f} reais.")
print(f"Novo preço com desconto de 5%:R${novo_preco:.2f} reais.")