"""
Escriba un programa que pregunte cuántos números se van a introducir,
pida esos números, y muestre un mensaje cada vez que un número no sea mayor 
que el anterior.
"""

print("MAYORES QUE EL ANTERIOR")

num1=int(input("¿Cuántos valores va a introducir? "))
acu=0

if num1 > 0:
    num2=int(input("Escriba un número: "))
    num3=int(input(f"Escriba un número más grande que {num2}: "))
    acu=num3
    for i in range(num1-2):
        num3=int(input(f"Escriba un número más grande que {acu}: "))
        if acu > num3:print(f"¡{num3} no es mayor que {acu}!")
    else:print("Gracias por su colaboración")
else:print("¡Imposible!")