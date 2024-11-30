'''
1. Escribe un programa que solicite al usuario dos números y muestre su
suma, resta, multiplicación, división, división entera y residuo (módulo).
'''
nombre=input("Hola, ¿Cual es tu nombre?")

print(f"Hola, {nombre}, vamos a realizar algunas operaciones matemáticas. Por favor, ingresa dos números:")
num1= float(input("Ingresa el primer numero"))
num2= float(input("ingresa el segundo numero"))

suma= num1+num2
resta= num1-num2
mult= num1*num2
exponente= num1**num2
division= num1/num2 if num2 !=0 else "No se puede dividir entre 0"
divisionEntera= num1//num2 if num2 !=0 else "No se puede dividir entre cero"
modulo= num1%num2 if num2 else "No se puede calcular el residuo"
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {mult}")