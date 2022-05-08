# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input("Digite uma temperatura em °C:"))
f = (c * 9/5) + 32
print(f"Temperatura de {c:.1f}C° corresponde a {f:.1f}F°")