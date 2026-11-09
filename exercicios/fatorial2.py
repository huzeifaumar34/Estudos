while True:
    try:
        numero = int(input("Insira um número: "))
        if numero < 0:
            print("Insira somente numeros positivos")
        else:
            resultado = 1
            for i in range(1, numero + 1):
                resultado *= i
            print(resultado)
            break
    except ValueError:
        print("Insira somente números inteiros")
