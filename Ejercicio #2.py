"""2.	Una empresa de llamadas al exterior tiene las siguientes tarifas: Estados Unidos: 900 pesos por minuto.
Canadá: 800 pesos por minuto. Europa: 950 pesos por minuto.
Resto del mundo: 1250 pesos por minuto.

Si la duración de la llamada es superior a 15 minutos, se aplica un descuento del 20% al valor de la llamada.
"""
print(" Se Hacen llamadas a USA, CANADA, EUROPA y el  RESTO DEL MUNDO")

print("* Para llamar a Estados unidos inserte el número 1")
print("*Para llamar a Canada inserte el número 2")
print("*Para llamar a Europa inserte el número 3")
print("*Para llamar  a el resto del mundo inserte el número 4")

Estados_unidos = 1
CANADA = 2
EUROPA = 3
RESTO_MUNDO = 4

COSTO_USA = 900
COSTO_CANADA = 800
COSTO_EUROPA = 950
COSTO_RESTO = 1250
Toda_la_Tarifa = 5

Pais = float(input("Inserte el número del país al que hará la llamada:"))
if Pais == 1:
    print("El costo de la llamada a EE.UU es de: ", COSTO_USA, "pesos por minuto")

if Pais == 2:
    print("Costo de la llamada a Cánada es de:", COSTO_CANADA, "Pesos por minuto")

if Pais == 3:
    print("El costo de la llamada a Europa es de:", COSTO_EUROPA, "pesos por minuto")

if Pais == 4:
    print("El costo de la llama al resto del mundo es de:", COSTO_RESTO, "Pesos por minuto")

Tiempo_Minutos = 15
Porcentaje = 20

TIEMPO_LLAMADA = float(input("*Ingrese el tiempo que tardó la llamada:"))

if TIEMPO_LLAMADA < 15:
    print("Pagas la tarifa plena del costo de la llamada")
    if Pais==1:
        print("tarifa plena:",COSTO_USA, "por cada minuto de la llamada")
    if Pais==2:
        print("tarifa plena:",COSTO_CANADA, "Por cada minuto de la llamada")
    if Pais==3:
        print("tarifa plena de", COSTO_EUROPA, "por cada minuto de la llamada")
    if Pais==4:
        print("tarifa plena:", COSTO_RESTO,"por cada minuto de la llamada")

if TIEMPO_LLAMADA >= 15:
    print("Obtienes un descuento del 20% por minuto de llamada, o sea:")

if Pais == 1:
 print( ((COSTO_USA)-COSTO_USA*Porcentaje/100),"pesos por minuto si tienes decuento")

if Pais == 2:
  print( ((COSTO_CANADA)-COSTO_CANADA*Porcentaje/100) , "pesos por minuto si tienes descuento")

if Pais == 3:
  print( ((COSTO_EUROPA)-COSTO_EUROPA*Porcentaje/100) , "pesos por minuto si tienes descuento")

if Pais == 4:
  print( ((COSTO_RESTO)-COSTO_RESTO*Porcentaje/100) , "pesos por minuto si tienes descuento")
































