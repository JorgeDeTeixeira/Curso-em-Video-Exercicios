from datetime import datetime
atual = datetime.today().year
totMaior = 0
totMenor = 0
for c in range(1, 8):
    pessoa = int(input(f"Digite o ano de nascimento da {c}° pessoa:"))
    idade = atual - pessoa
    if idade < 18:
        totMaior += 1
    else:
        totMenor += 1
print(f"Pessoas maiores de idade:{totMaior}")
print(f"Pessoas menor de idade:{totMenor}")