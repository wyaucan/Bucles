"""
Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y escriba el mayor,
el menor y la media aritmética. Se recuerda que la media aritmética de un conjunto de valores es la suma 
de esos valores dividida por la cantidad de valores.
"""

print("MAYOR, MENOR Y MEDIA ARITMÉTICA")

#temp=0
cont=0
mn=0
mx=0
v=0
n=int(input("¿Cuántos valores va a introducir? "))
if n > 0 :
    for i in range(n):
        n2=int(input(f"Escriba el número {i+1}: "))
        #cont=cont+n2
        if n2 > mx :
            mx=n2
        else:
            print("Positivo")
        
            
    #print("=", x)
    #print("El número más pequeño de los introducidos es:", v)
    print("El número más grande de los introducidos es:", mx)
       #print("El número más grande de los introducidos es:", ax2)
else:
    print("¡Imposible!")