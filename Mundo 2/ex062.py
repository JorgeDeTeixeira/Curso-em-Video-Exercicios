primeiro = int(input("Primeiro termo:"))
razao = int(input("Razão da PA:"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} -> ", end='')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos vo^ce quer mostrar a mais?"))
print(f"A PA foi finalizada com {total} termos.")