capital = float(input("Capital inicial: "))
taxa = float(input("Taxa mensal em %: "))
meses = int(input("Meses: "))

montante = capital * (1 + taxa / 100) ** meses

print(f"Montante: {montante:.2f}")
