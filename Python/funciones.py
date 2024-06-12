"""
    Modulo de ejemplo de definicion y uso de funciones en Python.
"""
# Parametros posicionales obligatorios
def funcion1(parametro1, parametro2):
    print(parametro1, parametro2)

    return "Valor de retorno"

retorno = funcion1(8, "Dale")
print(retorno)

# Valores por defecto | parametro opcional
def funcion2(parametro1, parametro2=8):
    print(parametro1, parametro2)
    return parametro1, parametro2

funcion2(10)
retorno = funcion2(10, 20)
print(retorno)

# Parametros por nombre
def division(dividendo, divisor):
    print(dividendo / divisor)

division(8, 4)
division(4, 8)

division(dividendo=8, divisor=4)
division(divisor=4, dividendo=8)

# Lambda 
cuadrado = lambda a : a ** 2

def cuadrado_funcion(a):
    """
        Calcula el cuadrado de un numero.

        parametros:
        a(int)
        return (float)
    """
    return a ** 2

print("-----------------------------------------")
print(cuadrado(5))
print(cuadrado_funcion(5))

lista = [7,6,1,2,3,5,8]

resultado = list(map(lambda a : a ** 2, lista))

print(resultado)