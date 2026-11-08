quantidade = int(input("Insira o número de termos: "))
a = 0
b = 1

for i in range(quantidade):
    print(a, end=" ")
    a, b = b, a + b

print()
