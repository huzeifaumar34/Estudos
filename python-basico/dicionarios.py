pessoa = {"nome": "Ana", "idade": 25}
print(pessoa["nome"])

pessoa["cidade"] = "Recife"
pessoa["idade"] = 26
print(pessoa)

print(pessoa.get("telefone", "não informado"))
print("nome" in pessoa)

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

nomes = ["Ana", "Paulo", "João", "Ana", "Maria", "João"]
contagem = {}
for nome in nomes:
    contagem[nome] = contagem.get(nome, 0) + 1
print(contagem)
