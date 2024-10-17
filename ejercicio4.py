"""
Programa que muestra la suma, resta, división y multiplicación de dos números dados
"""
# Versión con función
num1 = float(input ("Numero 1: "))
num2 = float(input ("Numero 2: "))
def operaciones_basicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2

    resultados = f"Suma: {suma}\nResta: {resta}\nMultiplicación: {multiplicacion}\nDivisión: {division}"
    return resultados
resultados = operaciones_basicas(num1, num2)
print(resultados)
