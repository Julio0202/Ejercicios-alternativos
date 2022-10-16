from tokenize import Exponent
print("Dime la base del exponente")
base = int(input())
print("Dime el exponente")
expon = int(input())
exponentes = 0
if expon>0:
    print("El resultado es", base**expon)
elif expon == 0:
    print("El resultado es 1")
else:
    exponentes = expon*-1
    print("El resultado es","1 /", base**exponentes)