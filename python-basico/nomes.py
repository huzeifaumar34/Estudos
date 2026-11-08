nomes = ["Ana", "Paulo", "João", "Ana", "Maria", "João"]

unicos = set(nomes)
print(f"Nomes Únicos: {len(unicos)}")
for nome in unicos:
    print(nome, nomes.count(nome))
