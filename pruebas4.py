def esDivisiblePor7(num):
    if num % 7 == 0:
        print(num ,"es un numero divisible por 7")
    else:
        print(num ,"no es un numero divisible por 7")


numero = int(input("Introduce el numero que quieres probar a dividir por 7: "))
esDivisiblePor7(numero)