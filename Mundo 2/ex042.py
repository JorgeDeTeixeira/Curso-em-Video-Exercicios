# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

p1 = float(input("Primeiro segmento:"))
p2 = float(input("Segundo segmento:"))
p3 = float(input("Terceiro segmento:"))

if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print("É possível formar uma trinângulo!")
    if p1 == p2 == p3:
        print("Tipo:EQUILÁTERO")
    elif p1 == p2 or p2 == p3 or p3 == p1:
        print("Tipo:ISÓSCELES")
    else:
        print("Tipo:ESCALENO")
else:
    print("Não é possível formar uma trinângulo!")