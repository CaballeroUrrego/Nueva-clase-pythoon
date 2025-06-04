punto = {"x":25, "y":50}	
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45

# Manejo seguro de claves no existentes
if "lala" in punto:
    print("Encontre lala", punto["lala"])

# .get() es una forma segura de acceder a claves
print(punto.get("x"))            # 25
print(punto.get("lala", 97))     # 97

# Eliminar claves correctamente
del punto["x"]
del punto["y"]

print(punto) 
punto = {"x": 25}

for valor in punto:
    print(valor,punto[valor])
    
for llave, valor in punto.items():
    print(llave,valor)
    
usuarios = [
    {"id": 1, "nombre": "Sebastián"},
    {"id": 2, "nombre": "Ana"},
    {"id": 3, "nombre": "Luis"},
    {"id": 4, "nombre": "Roxana"},
]

for usuario in usuarios:  
    print(usuario["id"], usuario["nombre"])