# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros
preco = float(input("Digite o preço do produto R$:"))
print('''Selecione o Metodo de Pagamento:
[1] Á vista dinheiro/cheque: 10% de desconto
[2] Á vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros
''')
opcao = int(input("Digite a forma de pagamento:"))
if opcao == 1:
    novo_preco = preco - (preco / 100 * 10)
    print(f"Preço antigo R$:{preco:.2f} reais")
    print(f"Com desconto de 10% R$:{novo_preco:.2f} reais")
elif opcao == 2:
    novo_preco = preco - (preco / 100 * 5)
    print(f"Preço antigo R$:{preco:.2f} reais")
    print(f"Com desconto de 10% R$:{novo_preco:.2f} reais")
elif opcao == 3:
    novo_preco = preco / 2
    print(f"Preço R$:{preco:.2f} reais")
    print(f"Parcelado em 2x. Com duas parcelas de R${novo_preco:.2f} reais")
elif opcao == 4:
    parcelas = int(input("Digite o total de parcelas desejadas:"))
    juros = preco + (preco / 100 * 20)
    novo_preco = juros / parcelas
    print(f"Preço antigoR$:{preco:.2f} reais")
    print(f"Total de parcelas:{parcelas}")
    print(f"Preço parcelado em {parcelas}R$:{novo_preco:.2f} reais com um juros de 20%.")
else:
    print("Opção Invalida!")