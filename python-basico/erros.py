try:
    numero = int(input("Digite um número: "))
    print(f"O dobro é {numero * 2}")
except ValueError:
    print("Isso não é um número válido!")

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Não dá para dividir por zero")
        return None

print(dividir(10, 0))
print(dividir(5, 0))

try:
    x = int(input("Outro número: "))
except ValueError:
    print("Inválido")
finally:
    print("Fim da tentativa")

while True:
    try:
        idade = int(input("Idade: "))
        break
    except ValueError:
        print("Digite apenas números.")
print(f"Idade registrada: {idade}")
