# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
kms = float(input("Km rodados:"))
dias = int(input("Dias alugados:"))
valor_dias = dias * 60
km_rodados = kms * 0.15
valor_final = valor_dias + km_rodados
print("-=-"*20)
print(f"KMs rodados{kms}")
print(f"Dias alugado:{dias}")
print(f"Preço por Km rodados R$:{km_rodados:.2f} reais")
print(f"Preço por dias alugado R$:{valor_dias:.2f} reais")
print("-=-"*20)
print(f"Valor total R$:{valor_final:.2f} reais")
print("-=-"*20)