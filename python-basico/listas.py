frutas = ["maçã", "banana", "uva"]
print(frutas[0])
print(frutas[-1])

frutas.append("manga")
frutas.remove("banana")
print(frutas)
print(len(frutas))

for fruta in frutas:
    print(f"Eu gosto de {fruta}")

print("uva" in frutas)

numeros = [5, 2, 9, 1]
numeros.sort()
print(numeros)
print(sum(numeros), max(numeros), min(numeros))
print(frutas[1:3])
print(frutas[10])

