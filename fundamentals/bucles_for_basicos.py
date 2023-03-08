# Tamaño grande
lista = [-1,3,4,5,-6]
def biggie_size(lista):
    for n in range(len(lista)):
        if lista[n] > 0:
            lista[n] = 'big'
    return lista

print(biggie_size(lista))


# Contar positivos
lista = [-2,-1,0,1,2,2,5,7,4]
def count_positives(lista):
    contador = 0
    for n in range(len(lista)):
       if lista[n] > 0:
           contador = contador + 1
    lista[-1] = contador
    return lista

print(count_positives(lista))

# Suma total
lista = [1,2,3,4,5,6,7]
def sum_total(lista):
    suma = 0
    for n in lista:
        suma = suma + n
    return suma
print(sum_total(lista))

# Promedio
lista = [1,2,3,4,5,6,7]
def average(lista):
    suma = 0
    for n in lista:
        suma = suma + n
        promedio = suma / len(lista)
    return promedio
print(average(lista))

# Longitud
lista = [1,2,3]
def length(lista):
    longitud = len(lista)
    return longitud
print(length(lista))

# Mínimo
lista = [-3,2,-4,4,5,6,7]
def minimum(lista):
    if len(lista) > 0:
        minimo = min(lista)
        return minimo
    else:
        return False
print(minimum(lista))
print(minimum([]))

# Máximo
lista = [-3,2,-4,4,5,6,7]
def maximum(lista):
    if len(lista) > 0:
        maximo = max(lista)
        return maximo
    else:
        return False
print(maximum(lista))
print(maximum([]))

# Análisis final
analisis = {'Suma':[], 'Promedio':[], 'Longitud':[], 'Minimo':[], 'Maximo':[]}
lista = [-3,2,-4,4,5,6,7]
def ultimate_analysis(lista):
    if len(lista) > 0:
        #Suma
        suma = 0
        for n in lista:
            suma = suma + n
        #Promedio
        suma = 0
        for n in lista:
            suma = suma + n
            promedio = suma / len(lista)
        #Longitud
        longitud = len(lista)
        #Minimo
        minimo = min(lista)
        #Maximo
        maximo = max(lista)
        return suma, promedio, longitud, minimo, maximo
    else:
        return False
    

analisis['Suma'].append(ultimate_analysis(lista)[0])
analisis['Promedio'].append(ultimate_analysis(lista)[1])
analisis['Longitud'].append(ultimate_analysis(lista)[2])
analisis['Minimo'].append(ultimate_analysis(lista)[3])
analisis['Maximo'].append(ultimate_analysis(lista)[4])
print(analisis)
#No logré que que las lineas de codigo 97 a 101 estuvieran incluidas dentro de la función.

# Lista inversa
lista = [-3,2,-4,4,5,6,7]
def reverse_list(lista):
    inversa = list(reversed(lista))
    return inversa

print(reverse_list(lista))