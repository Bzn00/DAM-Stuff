vidas = 7
for guess_num in range(1,7):
    print("Tienes ", vidas ," intentos")
    guess = input("Adivina la palabra: ").upper()
    while vidas > 0 and guess != "NIGGALAS":
        vidas = (vidas-1)
        print("Incorrecto, te quedan ", vidas, " vidas")
        guess = input("Introduce otro intento: ").upper()
        if vidas == 0:
            print("Te quedaste sin vidas")
            break
    if guess == "NIGGALAS":
        print("Correcto, eres un nigga")
        break