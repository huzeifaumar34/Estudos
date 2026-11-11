import random

opcoes = ["pedra", "papel", "tesoura"]

vence = {"pedra": "tesoura", "tesoura": "papel", "papel": "pedra"}

print("Digite pedra, papel ou tesoura")

while True:
    jogada = input(">> ").lower()
    computador = random.choice(opcoes)
    print()
    print(f"O computador escolheu: {computador}")
    if jogada not in opcoes:
        print("Jogada inválida!")
        print("Digite pedra, papel ou tesoura")
        continue
    elif jogada == computador:
        print("Empate!")
    elif vence[jogada] == computador:
        print("Você venceu!")
    else:
        print("Você perdeu!")
    op = input("Deseja continuar? (s/n) ").lower()
    if op == "s":
        continue
    else:
        break
