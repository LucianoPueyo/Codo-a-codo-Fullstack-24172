"""
    Colecciones de datos.

    Multiples datos contenidos en un mismo contenedor

    Listas:
        Son colecciones de elementos ordenados.

    Crear
    Consultar
    agregar
    quitar
    modificar
        

"""
# Creacion
lista_de_cualquier_cosa = [7, 1.5, "Hola", True, 6+1j, [1,2,3], None]

#         0   1   2   3
#        -4  -3  -2  -1
lista1 = [5,  6,  7,  8]

lista_vacia= []

lista2 = list(8,7,9)

# Acceder a valores
print(lista1)
print(lista1[0])

# indices negativos
print(lista1[-1]) # Ulitmo elemento

# fuera de rango
# lista1[9]

# Slice
print(lista1[1:3]) # Desde inclusive : Hasta no inclusive

# Iterando una lista
# For "clasico"
#          0         1        2       3
alumnos = ["Carlos", "Maria", "Jose", "Roberto"]

for i in range(len(alumnos)):
    print(alumnos[i])

print("-----------------------------")

# for each
for nombre_alumno in alumnos:
    print(nombre_alumno)

# Agregar valores
alumnos.append("Juana")
print(alumnos)

alumnos.insert(3, "Gaston")
print(alumnos)

# Quitar Valores
alumnos.pop()
print(alumnos)

alumnos.pop(3)
print(alumnos)

lista = [10, 11, 12, 10]
lista.remove(10)
print(lista)

# Modificar un valor
lista[2] = 125
print(lista)

# Ordenar lista
lista = [9,1,8,2,7,3,6,4,5,0]
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

# Existe

print(10 in lista)
print(8 in lista)