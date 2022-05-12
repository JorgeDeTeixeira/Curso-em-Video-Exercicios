Exércicio 42 - Mundo 2
# – IMC abaixo de 18,5: Abaixo do Peso

# – Entre 18,5 e 25: Peso Ideal

# – 25 até 30: Sobrepeso

# – 30 até 40: Obesidade

# – Acima de 40: Obesidade Mórbida

peso = float(input("Digite seu peso KG:"))
altura = float(input("Digite sua altura:"))
imc = peso / (altura ** 2)
print(f"Seu IMC:{imc:.2f}")
if imc < 18.5:
    print("Classificação:Abaixo do Peso")
elif 18.5 <= imc < 25:
    print("Classificação:Peso Ideal")
elif 25 <= imc < 30:
    print("Classificação:Sobrepeso")
elif 30 <= imc < 40:
    print("Classificação:Obesidade")
else:
    print("Classificação:Obesidade Mórbida")