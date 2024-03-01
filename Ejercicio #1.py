"""Ejercicio #1 Calcular y mostrar el indice de masa corporal de una persona"""

print("Calcular indice de masa corporal ")

Peso=float(input("Ingrese su peso en Kg:"))
print("Su peso es",Peso ,"kg")

Altura=float(input("Ingrese su altura en metros, Ejemplo 1.60:"))
print("Su altura es", Altura, "m")

IMC= Peso/(Altura*Altura)

print("Su indice de masa corporal es",IMC)

if IMC>=30:
    print("Tienes obesidad")
else:
    print("Tienes peso normal/Sobrepeso")







