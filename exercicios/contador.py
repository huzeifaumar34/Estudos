palavra = input("Digite uma palavra: ").split()

print(f"A frase tem {len(palavra)} palavras")
print(f"A palavra mais longa é {max(palavra, key=len)}")

