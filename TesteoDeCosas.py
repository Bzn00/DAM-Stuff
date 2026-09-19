#nombre = input("Introduce tu nombre: ").lower()
#nombre.lower()
#oculto = "*" * len(nombre)
#print(nombre)
#print("Vamos a encriptarlo")
#print("\n"*100)
#print(oculto)
#nombreaProbar = input("Adivina cual es el nombre: ").lower()
#if nombreaProbar == nombre:
#    print("Correcto!")
#else:
#    print("Incorrecto, era: ", nombre)

cantidadLista = int(input("Introduce el tamaño de la lista: "))

lista = []
for i in range(cantidadLista):
    objeto = input(f"Objeto nº ", i, ": ")
    lista.append(objeto)

print(lista)