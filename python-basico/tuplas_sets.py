ponto = (3, 5)
print(ponto[0])
x, y = ponto
print(f"x={x}, y={y}")

letras = {"a", "b", "c", "a", "b"}
print(letras)
letras.add("d")
print("a" in letras)

lista = [1, 2, 2, 3, 3, 3]
print(set(lista))
print(len(set(lista)))

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a & b)
print(a - b)
