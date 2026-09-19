cuenta = int(input("Introduce el dinero que vas a pagar: "))
propina = float(input("Introduce la propina que vas a querere dejar: "))
while propina > 20.0 or propina <= 0.0:
    propina = float(input("Introduce un porcentaje de propina valido (de 1 a 20)"))
cuentaTotal = cuenta + propina/100
print("Tu cuenta total es: ", cuentaTotal)