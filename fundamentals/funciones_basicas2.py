lista = []
def cuentaregresiva(numero):
    while numero >= 0:
        numero = numero - 1
        lista.append(numero + 1)
    print(lista)
cuentaregresiva(5)

######################

def print_and_return(num1, num2):
    print(num1)
    return(num2)
print_and_return(3,4)

######################

def first_plus_length(lista2):
    print(lista2[0] + len(lista2))

first_plus_length([1,2,3,4,5])

######################

def length_and_value(tamaño, valor):
    lista3 = [[valor]*tamaño]
    print(lista3)

length_and_value(6,10)

######################

lista_nueva = []
lista = []
def values_greater_than_second(lista):
    for valor in lista:
        if valor > valor[1]:
            lista_nueva.append(valor)
    print(lista)
    print(lista_nueva)

lista = [1,2,3,1,5,6]
values_greater_than_second(lista)