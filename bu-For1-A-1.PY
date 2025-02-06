"""
Escriba un programa que pida dos números enteros y escriba qué números son pares 
y cuáles impares desde el primero hasta el segundo.
"""

print("PARES E IMPARES")
num1=int(input("Escriba un número entero: "))
num2=int(input(f"Escriba un número entero mayor o igual que {num1}: "))

if(num1 <= num2):
    for n in range(num2):
        n+=1
        if(n>=num1):
            if(n % 2 == 0 ):
                print(f"El número {n} es par")
            else:
                print(f"El número {n} es impar")
        else:print
else:
    print(f"¡Le he pedido un número entero mayor o igual que {num1}!")
    