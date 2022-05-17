# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar

# [ 2 ] multiplicar

# [ 3 ] maior

# [ 4 ] novos números

# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.
opcao = 0
n1 = float(input("Primeiro valor:"))
n2 = float(input("Segundo valor:"))
while opcao != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input("Sua opção:"))
    if opcao == 1:
        print(f"A soma entre {n1} e {n2} é {n1 + n2}.")
    elif opcao == 2:
        print(f"A multiplicação entre {n1} e {n2} é {n1 * n2}.")
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f"O maior é {maior}")
        elif n2 > n1:
            maior = n2
            print(f"O maior é {maior}")
        else:
            print("Os dois são iguais!")
    elif opcao == 4:
        n1 = float(input("Primeiro valor:"))
        n2 = float(input("Segundo valor:"))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção invalida, tente novamente!")
print("Programa Finalizado, Obrigado!")