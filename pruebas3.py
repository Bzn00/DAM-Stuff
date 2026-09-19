def esPrimo(numero):
    if numero < 1:
        return print("No es primo")
    for i in range(2, numero):
        if numero % i == 0:
            return print("No es primo")
    return print("Es primo")

num = int(input("Introduce un numero por teclado: "))
esPrimo(num)