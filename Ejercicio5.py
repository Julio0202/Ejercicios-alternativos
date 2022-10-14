from numbers import Real
from socket import if_indextoname


infinito = 0
usuario = "Pepe"
real = "asdasd"
while (infinito==0):
    print("Dime un nombre de usuario")
    nomb = str(input())
    print("Dime una contraseña")
    contra = str(input())
    if nomb==usuario and contra==real:
        print("Has entrado")
        infinito = 1
    if(nomb!=usuario):
        print("Error en el usuario")
    else:
        print("Correcto el usuario")
    if(real!=contra):
        print("Error en la contraseña")
    else:
        print("Correcto en la contraseña")