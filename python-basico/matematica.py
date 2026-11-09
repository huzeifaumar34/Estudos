def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def eh_par(n):
    return n % 2 == 0

def media(*notas):
    return sum(notas) / len(notas)


