"""
 Programa que pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos
puntos en el plano. Calcula y muestra la distancia entre ellos.
"""
import math

x1 = float(input("Ingrese la coordenada x1: "))
y1 = float(input("Ingrese la coordenada y1: "))
x2 = float(input("Ingrese la coordenada x2: "))
y2 = float(input("Ingrese la coordenada y2:  "))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia entre los dos puntos es:", d)