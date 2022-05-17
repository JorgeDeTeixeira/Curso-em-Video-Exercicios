primeiro = int(input("Primeiro termo:"))
razao = int(input("Razão da PA:"))
c = 10
termo = primeiro
while c > 0:
    print(f"{termo} -> ", end='')
    termo += razao
    c -= 1
print("FIM")