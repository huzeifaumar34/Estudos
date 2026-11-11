import random

tentativas = 0
secreto = random.randint(1, 100)

while True:
    try:
        palpite = int(input("Adivinhe o número (1 a 100): "))
        tentativas += 1
        if palpite == secreto:
            print("Número correto!")
            print(f"Acertou em {tentativas} tentativas")
            break
        elif palpite > secreto:
            print("Muito alto!")
        elif palpite < 0:
            print("Insira somente números positivos")
        else:
            print("Muito baixo!")
    except ValueError:
        print("Insira somente números inteiros")

