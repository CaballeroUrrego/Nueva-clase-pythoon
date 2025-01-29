edad = int(input("Ingresa tu edad: "))

if edad > 65:
    print("Puedes ver la película con super descuento")
elif edad > 55:
    print("Puedes ver la película con descuento")
elif edad > 17:
    print("Puedes ver la película")
else:
    print("Debes irte")

print("Listo")