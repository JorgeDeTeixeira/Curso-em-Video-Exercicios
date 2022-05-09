from random import randint
from time import sleep

computador = randint(0, 5)
jogador = int(input("Tente acertar um número que eu pensei entra 0 e 5:"))
print("...")
sleep(2)
if jogador == computador:
    print("Você conseguiu acertar!")
else:
    print(f"Poxa, você perdeu! Eu pensei no {computador} e não no {jogador}!")