"""
Programa que leé un número y muestra su raíz cuadrada y su
raíz cúbica.
"""
import math
a = float(input("Ingrese un número: "))
R2 = math.sqrt(a)
R3 = a**(1/3)

print("La raíz cuadrada de", a, "es:",  R2)
print("La raíz cúbica de", a, "es:", R3)