"""
Escriba un programa que pregunte cuántos números 
se van a introducir, pida esos números, y diga al 
final cuántos han sido pares y cuántos impares.
"""

print("CONTADOR DE PARES E IMPARES")

n=int(input("¿Cuántos valores va a introducir? "))

i=0
acu1=0
acu2=0
if n > 0:
    for i in range(n):
        num2=int(input(f"Escriba el valor {i+1}: "))
        if num2 % 2 == 0:
            acu1=acu1+1
        else:
            acu2=acu2+1
    else:print(f"Ha escrito {acu1} números pares y {acu2} números impares."),print("Gracias por su colaboración.")
else:print("!Imposible!")


    
        
