#lista1 = [1,2,3,4]
#print(1,2,3,4)
#print(*lista)

#lista2 = [5,6]

#combinada = ["Hola", *lista1 ,"mundo", *lista2, "Chanchito"]
#print(combinada)

punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2, "lala": "hola mundo", "z": "mundo"}
print(nuevoPunto)
