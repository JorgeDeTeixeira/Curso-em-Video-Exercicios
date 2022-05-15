# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
hVelho = 0
homem_velho = ''
mMenos20 = 0
for c in range(1, 5):
    print(F"{c}° Pessoa:")
    nome = str(input(f"Nome:")).strip()
    idade = int(input("Idade:"))
    sexo = str(input("Sexo:")).strip().upper()[0]
    media += idade
    if c == 1 in sexo == 'M':
        hVelho = idade
        homem_velho = nome
    else:
        if idade > hVelho in sexo == 'M':
            hVelho = idade
            homem_velho = nome
    if sexo == 'F':
        mMenos20 += 1
print(F"Média da idade do grupo:{media/4:.2f}")
print(f"Homem mais velho se chama {homem_velho.capitalize()} com {hVelho} anos")
print(f"Total de {mMenos20} com menos de 20 anos.")