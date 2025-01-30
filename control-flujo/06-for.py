#Buscar ellementos de operaciones matematicas
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontré el número buscado :(")
    for char in "Caballero jugando con py":
        print(char)