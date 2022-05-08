# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
din = float(input("Quanto você tem na carteira?"))
dolar = din / 5.08
print(f"Com R${din:.2f} você pode comprar U${dolar:.2f} dolár(res)")