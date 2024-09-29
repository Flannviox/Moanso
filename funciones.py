print("Calculadora xd")

def multiplicar(x,y):
    a = x*y
    return print(f"La multiplicación de {x} y {y} es {a}")

def potencia():
    base = float(input("ingrese la base: "))
    exponente = float(input("Ingrese el exponente: "))
    resultado = base ** exponente
    print (f"{base} elevado a {exponente} es:  {resultado}")

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

def restar (a,b):

    return a-b

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

resultado = restar(num1, num2)

print(f"La resta de {num1} - {num2} es: {resultado}")