def somar_tudo(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(somar_tudo(1, 2))
print(somar_tudo(1, 2, 3, 4, 5))

def mostrar_perfil(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

mostrar_perfil(nome="Ana", idade=26, cidade="Recife")
