"""
Escriba un programa que pregunte cuántos números se van a introducir, 
pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.
"""
print("MAYORES QUE EL PRIMERO")
num1=int(input("¿Cuántos valores va a introducir?: "))

if(num1 > 0):
    num2=int(input("Escriba un número: "))
    for i in range(num1-1):
        num3=int(input(f"Escriba un número más grande que {num2}: " ))
        if(num2 < num3):
            print
        else:print(f"{num3} no es mayor que {num2}")
    print("Gracias por su colaboración.")
else:print("¡Imposible!")