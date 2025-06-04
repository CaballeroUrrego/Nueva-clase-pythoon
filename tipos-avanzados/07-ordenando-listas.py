numeros = [ 2, 4, 1, 45, 75, 22]
# Ordenar una lista
#numeros.sort(reverse=True)  # Ordena la lista en orden descendente
numeros2= sorted(numeros,reverse=True)  # Ordena la lista en orden ascendente, pero no modifica la lista original
print(numeros)
print(numeros2)  # Imprime la lista ordenada

usuarios =[
    ["Chanchito",4],
           ["Feleipe",1],
           ["pulga",5]
]

#def ordena (elemento):
  #  return elemento[1] 

# Ordena por el segundo elemento de cada sublista
#usuarios.sort(key=ordena, reverse=True)  # Ordena la lista de usuarios en orden descendente por el segundo elemento
usuarios.sort(key=lambda el : el[1],reverse=True)

print(usuarios)