mascotas = [ 
            'wolfgang',
            'pelusa', 
            'pulga', 
            'felipe',
             'pulga',
            'Chanchito feliz'
]
mascotas.insert(1,"Lucius" )
mascotas.append("Chanchito triste")

mascotas.remove("pulga")
mascotas.pop(1)
del mascotas[0]  
mascotas.clear()  # Elimina todos los elementos de la lista
print(mascotas)