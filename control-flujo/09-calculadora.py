print("Bienvenidos a la calculadora")
print("Para salir escribir 'salir'")
print("Las operaciones son suma, resta, multi y div")

resultado = None

while True:
    if resultado is None:
        resultado = input("Ingrese un número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    else:
        op = input("Ingrese la operación: ")
        if op.lower() == "salir":
            break

        n2 = input("Ingresa siguiente número: ")
        if n2.lower() == "salir":
            break
        n2 = int(n2)

        if op.lower() == "suma":
            resultado += n2
        elif op.lower() == "resta":
            resultado -= n2
        elif op.lower() == "multi":
            resultado *= n2
        elif op.lower() == "div":
            if n2 == 0:
                print("Error: No se puede dividir por cero.")
                continue
            resultado /= n2
        else:
            print("Operación no válida")
            continue

        print(f"El resultado es: {resultado}")
