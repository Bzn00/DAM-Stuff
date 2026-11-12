def esAnagrama(palabra1, palabra2):
    for letras in palabra1:
        if palabra1.count(letras) == palabra2.count(letras):
            iguales = True
        else:
            iguales = False
    if iguales == True:
        return print("Es un anagrama ", iguales)
    else:
        return print("No es un anagrama ", iguales)



palabra1 = "casa"
palabra2 = "caca"

esAnagrama(palabra1.lower(), palabra2.lower())
