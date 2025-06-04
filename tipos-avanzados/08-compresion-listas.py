from subprocess import list2cmdline


usuarios =[
    ["Chanchito",4],
           ["Feleipe",1],
           ["pulga",5]
]

#nombres= []
#for usuario in usuarios:
#    nombres.append(usuario[0])
#print(nombres)
#nombres = [usuario[0] for usuario in usuarios]
#nombres = [usuario  [0] for usuario in usuarios if usuario[1] > 2]
# nombres =list(map(lambda usuario:usuarios[0], usuarios))

MenosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(MenosUsuarios)

