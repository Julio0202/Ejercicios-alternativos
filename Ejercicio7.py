print("Dime la base del exponente")
base = int(input())
print("Dime el expontente")
expon = int(input())
res = base
if(expon>1):
    while (expon>1):
        res=res*base
        expon = expon-1
    print("El resultado es", res)
elif(expon==0):
    print("El resultado es 1")
elif(expon<1):
    while (expon<1):
        res=res*base
        expon = expon-1
    print("El resultado es", "1 /", res)

