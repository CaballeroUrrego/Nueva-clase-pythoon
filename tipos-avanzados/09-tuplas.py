numeros = (1, 2, 3) + (4, 5, 6)  # Se concatenan dos tuplas
print(numeros)  # (1, 2, 3, 4, 5, 6)

punto = tuple([1, 2])  # Se convierte una lista en tupla
print(punto)  # (1, 2)

menosNumeros = numeros[:2]  # Se hace slicing (del índice 0 al 1)
print(menosNumeros)  # (1, 2)

primero, segundo, *otros = numeros  # Desempaquetado
print(primero, segundo, otros) 

for n in numeros:  
    print(n)  

listaNumeros = list(numeros)  
listaNumeros[0] = "Chanchito feliz"  
print(listaNumeros)  
