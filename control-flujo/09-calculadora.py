print("Bienvenidos a la calculadora:Alejandro")  # Mensaje de bienvenida
print("Para salir escribir 'salir'")  # Instrucción para salir del programa
print("Las operaciones son suma, resta, multi y div")  # Lista de operaciones disponibles

resultado = None  # Inicializamos la variable resultado como None

while True:  # Bucle infinito hasta que el usuario decida salir
    if resultado is None:  # Si resultado es None, pedimos el primer número
        resultado = input("Ingrese un número: ")  # Solicitamos al usuario que ingrese un número
        if resultado.lower() == "salir":  # Si el usuario escribe 'salir', terminamos el programa
            break
        resultado = int(resultado)  # Convertimos el número ingresado a entero
    else:  # Si resultado ya tiene un valor, pedimos la operación y el siguiente número
        op = input("Ingrese la operación: ")  # Solicitamos al usuario que ingrese una operación
        if op.lower() == "salir":  # Si el usuario escribe 'salir', terminamos el programa
            break

        n2 = input("Ingresa siguiente número: ")  # Solicitamos al usuario que ingrese el siguiente número
        if n2.lower() == "salir":  # Si el usuario escribe 'salir', terminamos el programa
            break
        n2 = int(n2)  # Convertimos el número ingresado a entero

        if op.lower() == "suma":  # Si la operación es suma
            resultado += n2  # Sumamos n2 a resultado
        elif op.lower() == "resta":  # Si la operación es resta
            resultado -= n2  # Restamos n2 a resultado
        elif op.lower() == "multi":  # Si la operación es multiplicación
            resultado *= n2  # Multiplicamos resultado por n2
        elif op.lower() == "div":  # Si la operación es división
            if n2 == 0:  # Si n2 es 0, mostramos un mensaje de error
                print("Error: No se puede dividir por cero.")
                continue  # Continuamos con la siguiente iteración del bucle
            resultado /= n2  # Dividimos resultado por n2
        else:  # Si la operación no es válida
            print("Operación no válida")  # Mostramos un mensaje de error
            continue  # Continuamos con la siguiente iteración del bucle

        print(f"El resultado es: {resultado}")  # Mostramos el resultado actual