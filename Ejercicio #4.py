"""4.	Escribir un algoritmo que lea las cuatro notas (de 1 a 5) de un estudiante y permita clasificar su rendimiento de acuerdo con el promedio de la siguiente forma:
Entre 4 y 5: excelente
Ente 3 y 3.99: Bien
Entre 0 y 2,99: Deficiente
Adicionalmente, se otorga un descuento en la matrícula del 20% para aquellos estudiantes que obtienen un rendimiento excelente,
de lo contrario paga el 100% del costo de la matrícula.
 ¿Cuánto tiene que pagar el estudiante?
"""

Nota1 = float(input("Ingrese la nota #1:"))
if Nota1 >= 4.0 and Nota1 <= 5.0:
    print("Tienes rendimiento excelente de:", Nota1)
if Nota1 >= 3.0 and Nota1 <=3.99:
    print("Tienes rendimiento bueno de:", Nota1)
if Nota1 >= 0 and Nota1 <= 2.99:
    print("Tienes un rendimiento deficiente de :",Nota1)

Nota2= float(input("Ingrese la nota #2:"))

if Nota2 >= 4.0 and Nota2 <= 5.0:
    print("Tienes rendimiento excelente de:", Nota2)
if Nota2 >= 3.0 and Nota2 <=3.99:
    print("Tienes rendimiento bueno de:", Nota2)
if Nota2 >= 0 and Nota2 <= 2.99:
    print("Tienes un rendimiento deficiente de :",Nota2)

Nota3 = float(input("Ingrese la nota #3:"))
if Nota3 >= 4.0 and Nota3 <= 5.0:
    print("Tienes rendimiento excelente de:", Nota3)
    if Nota3 >= 3.0 and Nota2 <=3.98:
        print("Tienes rendimiento bueno de:", Nota3)
if Nota3 >= 0 and Nota3 <= 2.99:
    print("Tienes un rendimiento deficiente de :", Nota3)

Nota4 = float(input("Ingrese la nota #4:"))

if Nota4 >= 4.0 and Nota4 <= 5.0:
    print("Tienes rendimiento excelente de:", Nota4)
if Nota4 >= 3.0 and Nota4 <=3.99:
    print("Tienes rendimiento bueno de:", Nota4)
if Nota4 >= 0 and Nota4 <= 2.99:
    print("Tienes un rendimiento deficiente de :", Nota4)

numero=((Nota3+Nota1+Nota4+Nota2)/4)
print("Tu promedio acumulado es:",numero)

des=20

if numero >= 4.0:
    print("Obtienes un descuento del 20%=", (numero*des)/100, "%", "del total de la matrícula")

else:
    print("Pagas el 100% de la matrícula")










