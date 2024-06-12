"""
    Los diccionarios de python son como Objectos de Javascript (Arrays asociativos)

    Los diccionarios no poseen orden.

    json:
    {
        "nombre": "Carlos",
        "edad": 25,
        "turno": "Mañana"
    }

    Python
    {
        alumno1: {
            "nombre": "Carlos",
            "edad": 25,
            "turno": "Mañana"
        },

        alumno2: {
            "nombre": "Carlos",
            "edad": 25,
            "turno": "Mañana"
        },
    }
"""

diccionario1 = {
    "nombre": "Carlos",
    "edad": 25,
    "turno": "Mañana",
    "Curso": "Fullstack"
}

print(diccionario1["nombre"])
print(diccionario1["edad"])
print(diccionario1["turno"])

print("----------------------")
# Iteracion
# For each
for clave in diccionario1:
    print(clave, diccionario1[clave])

print("----------------------")
# keys, values, items
for clave in diccionario1.keys():
    print(clave, diccionario1[clave])

print("----------------------")
for valor in diccionario1.values():
    print(valor)

print("----------------------")
for clave, valor in diccionario1.items():
    print(clave, valor)

# Agregar valor
diccionario1["curso"] = "Fullstack Python"
print(diccionario1)

# Modificar valor
# Las claves en un diccionario son unicas
diccionario1["nombre"] = "Roberto"
print(diccionario1)

del diccionario1["curso"]
print(diccionario1)

alumno1 = {
    "nombre": "Carlos",
    "edad": 25,
    "turno": "Mañana"
}
alumno2 = {
    "nombre": "Maria",
    "edad": 25,
    "turno": "Mañana"
}
alumno3 = {
    "nombre": "Jose",
    "edad": 25,
    "turno": "Mañana"
}

lista = [
    alumno1,
    alumno2,
    alumno3
]



alumnos = {
    "alumno1": {
        "nombre": "Carlos",
        "edad": 25,
        "turno": "Mañana"
    },
    "alumno2": {
        "nombre": "Maria",
        "edad": 30,
        "turno": "Noche"
    },
}

print(alumnos["alumno1"])

del alumnos["alumno1"]["turno"]
print(alumnos["alumno1"])