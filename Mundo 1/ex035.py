p1 = float(input("Primeiro segmento:"))
p2 = float(input("Segundo segmento:"))
p3 = float(input("Terceiro segmento:"))

if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print("É possível formar uma trinângulo!")
else:
    print("Não é possível formar uma trinângulo!")