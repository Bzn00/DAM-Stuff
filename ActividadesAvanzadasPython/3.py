import random
vidas = 5
numRandom = random.randint(1, 50)


guess = int(input("Introduce un numero aleatorio del 1 al 50, para ver si lo adivinas: "))
while guess > 50 or guess <= 0:
    guess = int(input("Introduce un numero aleatorio del 1 al 50, para ver si lo adivinas: "))


if guess == numRandom:
    print("Adivinaste, el numero aleatorio era: ", numRandom)
else:
    while guess != numRandom and vidas != 0:
        vidas-=1    
        guess = int(input(f"Fallaste, te quedan {vidas} vidas: "))
    if vidas == 0:
        print("Se acabo el juego, perdiste, el numero era: ", numRandom)



