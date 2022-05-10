# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
ano = int(input("Digite o seu ano de nascimento:"))
idade = atual - ano
print(f"Você nasceu em {ano} e tem {idade} em {ano}")
if idade == 18:
    print("Você se alistara esse ano!")
elif idade < idade:
    falta = 18 - idade
    anos = atual + falta
    print(f"Falta {falta} anos para o seu alistamento!")
    print(f"Seu alistamento será em {anos}")
else:
    falta = idade - 18
    anos = atual - falta
    print(f"Passou {falta} anos do seu alistamento!")
    print(f"Seu alistamento foi em {anos}")