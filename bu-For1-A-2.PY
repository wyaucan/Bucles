"""
Escriba un programa que pida un número entero mayor que cero 
y que escriba sus divisores.
"""

print("DIVISORES")
num=int(input("Escriba un número mayor que cero: "))

acu=0
if(num > 0):
    for n in range(num):
        n+=1
        if(num % n == 0):
            print(n)
else:print("¡Le he pedido un número entero mayor que cero!")