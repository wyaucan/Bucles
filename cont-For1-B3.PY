"""Escriba un programa que pida un número entero mayor 
que 1 y que escriba si el número es un número primo o no.
"""
n=int(input("¿Cuántos valores va a introducir? "))

print("NÚMERO PRIMO")
if n > 0:
    for i in range(2,n):
        if(n % i == 0):
            print("No es primo")
            break
        else:
            print("Es primo") 
            break
    if(n==1):print("No es primo")
    if(n==2):print("es primo")
else:print(f"¡Le he pedido un número entero mayor que {n}!")