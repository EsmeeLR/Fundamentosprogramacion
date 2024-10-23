"""
Programa que pide al usuario dos pares de números (x1,y2) y (x2,y2), 
que representen dos puntos en el plano y calcula la distancia entre ellos.
"""
x1 = int(input("¿Cuál es el valor de x1? "))
x2 = int(input("¿Cuál es el valor de x2? "))
y1 = int(input("¿Cuál es el valor de y1? "))
y2 = int(input("¿Cuál es el valor de y2? "))

distancia = (((x2 - x1)**2 + (y2 - y1)**2)) 0.5
print("La distarncia entre los puntos es:",distancia)
