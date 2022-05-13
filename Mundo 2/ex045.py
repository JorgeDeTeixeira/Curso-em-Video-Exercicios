from random import randint
from time import sleep
computador = randint(0, 2)
esc = ['PEDRA', 'PAPEL', 'TESOURA']
print("Vamos jogar um jogo?")
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")
jogador = int(input("Escolha uma opção:"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO...")
print("-=-"*10)
print(f"Computador escolheu {esc[computador]}")
print(f"Jogador escolheu {esc[jogador]}")
print("-=-"*10)
if computador == 0: # Computador escolheu PEDRA
    if jogador == 0: # Jogador escolheu PEDRA
        print("EMPATE!")
    elif jogador == 1: # Jogador escolheu PAPEL
        print("VOCÊ GANHOU!")
    elif jogador == 2: # Jogador escolheu TESOURA
        print("VOCÊ PERDEU!")
    else:
        print("ESCOLHA INVALIDA!")
elif computador == 1: # Computador escolheu PAPEL
    if jogador == 0: # Jogador escolheu PEDRA
        print("VOCÊ PERDEU!")
    elif jogador == 1: # Jogaodor escolheu PAPEL
        print("EMPATE")
    elif jogador == 2: # Jogodor escolheu TESOURA
        print("VOCÊ GANHOU!")
    else:
        print("OPÇÃO INVALIDA")
elif computador == 2: # Computador escolheu TESOURA
    if jogador == 0: # Jogador escolheu PEDRA
        print("VOCÊ GANHOU!")
    elif jogador == 1: #Jogador escolheu PAPEL
        print("VOCÊ PERDEU!")
    elif jogador == 2: #Jogaodr escolheu TESOURA
        print("EMPATE")
    else:
        print("OPÇÃO INVALIDA")