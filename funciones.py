
# SUMAR
def sumar(a, b):
    return a + b

def sumar(lista):
    total = 0
    for i in lista:
        total += i

    return total

print("Ingresa la cantidad de numeros que quieres sumar")
cantidad = int(input())
lista=[]
for i in range(cantidad):
    print("ingresa el valor numero ", i+1)
    num = int(input())  
    lista.append(num)

print(lista)
print("La suma total es: ", sumar(lista))


# MULTIPLICAR

def multiplicar(x,y):
    a = x*y
    return print(f"La multiplicación de {x} y {y} es {a}")

def potencia():
    base = float(input("ingrese la base: "))
    exponente = float(input("Ingrese el exponente: "))
    resultado = base ** exponente




