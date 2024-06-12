"""
    Las tuplas son muy parecidas a las listas (Coleccion de elementos ordenados) pero son INMUTABLES.

    Es decir, una vez que creamos una tupla, no puedo modificarla.

    Operaciones
    Crear
    Consultar
    Buscar
"""

def funcion():
    return 1,2,3

# Las funciones, cuando devuelven mas de un valor, lo hacen a traves de una tupla.
print(funcion(), type(funcion()))

# Creacion
tupla1 = ("Carlos", "Maria", "Jose")

print("Carlos" in tupla1)

# Iteracion
# For "Clasico"
for i in range(len(tupla1)):
    print(tupla1[i])

print("-----------------------------------")
# For each
for nombre in tupla1:
    print(nombre)