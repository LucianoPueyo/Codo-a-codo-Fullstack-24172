# Variable global
a = 10
VALOR_CONSTANTE = 50

def funcion():
    # Variable local
    b = 50
    print(a)

funcion()
print(a)

# Variables locales no pueden ser accedidas desde un scope externo
# print(b)