-- Sumar
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

-- Restar
def restar (a,b):

    return a-b

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

resultado = restar(num1, num2)

print(f"La resta de {num1} menos {num2} es: {resultado}")