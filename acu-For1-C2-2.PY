"""
Mejore el programa anterior haciendo que el programa escriba la suma realizada.
"""

print("SUMA ENTRE VALORES")
n1=int(input("Escriba un número entero positivo: "))

acu=0
total=0

if n1 > 0:
        n2=int(input(f"Escriba un número entero mayor que {n1}: "))
        if(n1 == n2):
               print(f"¡Le he pedido un número entero mayor que {n1}!")
        else:
                for i in range(n1):
                        print   
                for j in range(1, n2):
                        if(j >= n1):
                                acu=acu+j
                                total=acu+n2
                                print(f"{j}", end=" + ") #Para que muestre encadena los numeros.
                        else:
                                print
                print(f"{n2} =",total)        
                #print(j+1)
else:
        print("¡Le he pedido un número entero positivo!")
        
    