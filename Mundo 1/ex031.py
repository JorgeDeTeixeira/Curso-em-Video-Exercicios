# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = float(input("Digite a distancia da viagem Km:"))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print(f"Valor da viagem R$:{preco:.2f} reais.")