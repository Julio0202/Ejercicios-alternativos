print("Dime tu nota")
nota = int(input())
print("Dime tu edad")
edad = int(input())
print("Dime tu sexo, F o M")
sexo = str(input())

if nota>=5 and edad>=18 and sexo=="F":
    print("Aceptada")
elif nota>=5 and edad>=18 and sexo=="M":
    print("Posible")
else:
    print("No es posible")