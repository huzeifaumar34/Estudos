peso = float(input("Insira o peso (kg): "))
altura = float(input("Insira a altura (m): "))

imc = peso / altura ** 2

print(f"IMC: {imc:.1f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")

