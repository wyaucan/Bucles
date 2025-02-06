"""Escriba un programa que pregunte cuántos números se van a introducir,
    pida esos números y escriba cuántos negativos ha introducido.
"""

print("NÚMEROS NEGATIVOS")
num1=int(input("¿Cuántos valores va a introducir? "))

acu=0
if num1 > 0: 
    for i in range(num1):
        num2 = int(input(f"Escriba el número {i+1}: "))    
        if num2 > 0:
            print
        else:
            acu=acu+1
    print(f"hasta escrito {acu} número negativo.") 
elif num1 == 0:print("No ha escrito ningún número negativos.")
else:print("¡Imposible!")