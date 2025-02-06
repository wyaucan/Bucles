"""
Escriba un programa que pregunte cuantos números se van a introducir, 
pida esos números (que puedan ser decimales) y calcule su suma.
"""

print("SUMA DE VALORES")

acu=0
n1=int(input("¿Cuántos valores va a introducir? "))
if n1 > 0:
    for i in range(n1):
        n2=float(input(f"Escriba el número {i+1}: "))
        acu=acu+n2
    else:print(f"La suma de los números que ha escrito es {acu} ")
else:print("¡Imposible!")