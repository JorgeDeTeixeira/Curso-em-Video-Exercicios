# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velo = float(input("Digite a velocidade do carro:"))
if velo > 80:
    multa = (velo - 80) * 7.0
    print(f"Você foi multado, Valor R$:{multa:.2f} reais.")
print("Tenha um bom dia, Dirija com cuidado!")