idade = int(input("Quantos anos você tem? "))

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")

tem_ingresso = False

if idade >= 18 and tem_ingresso:
    print("Pode entrar")
else:
    print("Não pode entrar")
