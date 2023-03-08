import random
def randInt(minimo=0, maximo=100):
    maximo = maximo + 1
    print(f'Valor minimo: {minimo}, valor maximo: {maximo}')

    num = round((random.random() * maximo) + minimo)
    return num

#Número entre 0 y 100
print(randInt())

#Numero entre 0 y 50
print(randInt(maximo=50))

#Numero entre 50 y 100
print(randInt(minimo=50))


#Numero entre 50 y 500
print(randInt(minimo=50,maximo=500))
