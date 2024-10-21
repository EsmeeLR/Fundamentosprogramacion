"""
Programa que calcula cual será la calificación final de un alumno en la materia de Algoritmos.
"""
P1 = int(input("Ingresa la calificación del primer parcial: "))
P2 = int(input("Ingresa la calificación del segundo parcial: "))
P3 = int(input("Ingresa la calificación del tercer parcial: "))
Ex_final = int(input("Ingresa la calificación del examen final: "))
T_final = int(input("Ingresa la calificación del trabajo final: "))
promedio_cp = (P1 + P2 + P3)/3
cal_final = (promedio_cp * 0.55) + (Ex_final * 0.3) + (T_final * 0.15)
print("La calificación  final es: ", cal_final)
