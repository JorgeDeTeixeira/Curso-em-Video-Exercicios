from random import randint
computador = randint(0, 11)
tent = 1
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
jogador = int(input("Qual o seu palpite?"))
while computador != jogador:
    tent += 1
    if jogador > computador:
        print("Menos... Tente mais uma vez.")
        jogador = int(input("Qual o seu palpite?"))
    elif jogador < computador:
        print("Mais... Tente mais uma vez.")
        jogador = int(input("Qual o seu palpite?"))
print(F"Acertou com {tent} tentativas. Parabéns.")