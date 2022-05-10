# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número:"))
print('''
[1] Converter para BÍNARIO
[2] Converter para HEXADECIMAL
[3] Converter para OCTAL''')
opcao = int(input("Sua opção:"))
if opcao == 1:
    print(F"{num} Convertido para BÍNARIO é igual a {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} Convertido par HEXADECIMAL é igual a {hex(num)[2:]}")
elif opcao == 3:
    print(f"{num} Convertido para OCTAL é igual a {oct(num)[2:]}")
else:
    print("Opçaõ invalida!")