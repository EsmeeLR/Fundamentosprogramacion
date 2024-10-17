"""
Programa que convierte un valor dado ppor el usuario en grados Farenheit a grados Celsius
"""
# Conversión de Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Solicitar al usuario el valor en Fahrenheit
fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))

# Convertir y mostrar el resultado
celsius = fahrenheit_a_celsius(fahrenheit)
print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius.")
