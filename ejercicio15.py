"""
 Dadas dos variables numéricas A y B,
realizar un programa que intercambie los valores de ambas variables y muestre
cuanto valen al final las dos variables.   
"""

A = float(input("Introduce el valor de A: "))
B = float(input("Introduce el valor de B: "))

print("Valores originales  A:", A, "B:", B)
temp = A
A = B
B = temp
print("Valores intercambiados  A:", A, "B:", B)
