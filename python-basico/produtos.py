produtos = {"Placa de vídeo": 5000, "Teclado": 1000, "Mouse": 500}

print(produtos)

total = sum(produtos.values())

print(f"Total: {total}")

for nome, preco in produtos.items():
    print(f"{nome} : R$ {preco}")


