from operator import truediv
print("Dime un número")
num1 = int(input())
print("Dime otro")
num2 = int(input())
print("Dime otro")
num3 = int(input())
lista = []
lista.append(num1)
lista.append(num2)
lista.append(num3)
lista.sort(reverse=True)
print(lista)

print("El mayor es", lista[0])
ultimo = len(lista)
print("El menor es", lista[ultimo-1])