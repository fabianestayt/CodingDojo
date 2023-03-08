# 1. Básico
for x in range(151):
    print(x)

# 2. Múltiplos de cinco
for x in range(5, 1001, 5):
    print(x)

# 3. Contar al estilo Dojo
for x in range(1, 101):
    if x % 10 == 0:
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')
    else:
        print(x)

# 4. Whoa. Es un gran idiota
lista = []
for x in range(500001):
    if x % 2 != 0:
        lista.append(x)
print(sum(lista))

# 5. Cuenta regresiva de 4 en 4
for x in range(2018, 0, -4):
    print(x)

# 6. Contador flexible
lowNum = 1
highNum = 22
mult = 3
for x in range(lowNum, highNum):
    if x % mult == 0:
        print(x)