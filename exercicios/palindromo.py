palavra = input("Digite uma palavra: ").lower().replace(" ", "")

texto = palavra

if texto[::-1] == palavra:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

