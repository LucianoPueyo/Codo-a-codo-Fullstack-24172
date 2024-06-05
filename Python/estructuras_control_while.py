seguir = True
contador = 0
while seguir:
    print(contador)
    contador += 1

    if(contador == 10):
        break


# Ojo con los loops infinitos
"""
contador = 0
while True:
    print(contador)
    contador+=1
"""