
print("Lugares disponibles para llamar, escribalos de forma exacta en el cuestionario:  Estados unidos, Canada, Europa, RestoMundo")

E
Lugar_llamada = input("Ingrese el destino de la llamada:")
Duracion_llamada = float(input("ingrese la duración de la llamada en minutos:"))

if Lugar_llamada == "Estados unidos":
    precio = 900
elif Lugar_llamada == "Canada":
    precio = 800
elif Lugar_llamada == "Europa":
    precio = 950

elif Lugar_llamada == "RestoMundo":
    precio = 1250

Valor_Pleno= precio*Duracion_llamada
Valor_Llamada = precio*Duracion_llamada

if Duracion_llamada < 15:
    print("Pagas ")

if Duracion_llamada > 15:
    descuento = Valor_Llamada*0.2
    Valor_Llamada = Valor_Llamada-descuento


print("El costo de la llamada es " , Valor_Llamada ,"$ Pesos")
