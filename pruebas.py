def menu():
    print("1. Decir hola")
    print("2. mostrar edad")
    opcion = int(input("Introduce una opcion: "))
    while opcion != 1 and opcion != 2:
        print("1. Decir hola")
        print("2. mostrar edad")
        opcion = int(input("Introduce una opcion valida: "))
    if opcion == 1:
        print("Hola banda :D")
    elif opcion == 2: 
        print("Tu edad es: ", num)
    


num = int(input("Introduce tu edad: "))
if num >= 18:
    print("Eres mayor de edad")
    menu()
elif num < 18:
    print("Eres menor de edad, no puedes acceder a este programa.")
else: 
    print("Introduce un numero valido..")


