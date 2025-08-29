import math
import random

#Ejercicio 1:
for i in range(101):
    print(i)

#Ejercicio 2:
numero = int(input("Ingrese un numero entero "))
digitos = 0
aux = numero
while aux > 0:
    aux = math.trunc (aux / 10)
    digitos = digitos + 1
print (f"El numero {numero} tiene en total {digitos} digitos")

#Ejercicio 3:
num1 = int(input("Ingrese un primer numero "))
num2 = int(input("Ingrese un segundo numero "))
resultado = 0
for i in range(num1+1,num2):
    resultado = resultado + i

print(f"La suma de todos los numeros desde {num1} hasta {num2} excuyendolos es: {resultado}")

#Ejercicio 4:
suma = 0
while True:
    numero = int(input("Ingrese cualquier numero, para salir ingrese 0\n"))
    if numero != 0:
        suma = suma + numero
    else:
        break
print(f"El total de la suma de todos los numeros ingresados es: {suma}")

#Ejercicio 5:
numAleatorio = random.randint(0,9)
intentos = 0
while True:
    numero = int(input("Adivine el numero aleatorio entre 0 y 9\n"))
    intentos = intentos + 1
    if numero == numAleatorio:
        print (f"Correcto, te tomo {intentos} intentos advinar el numero")
        break
    else:
        print("Incorrecto, vuelva a intentar")

#Ejercicio 6:
print("Estos son todos los numeros pares desde el 100 hasta el 0")
for i in range(100,-1,-2):
    print(i)

#Ejercicio 7:
suma = 0
while True:
    numero = int(input("Ingrese un numero mayor a 0 "))
    if numero > 0:
        for i in range(0,numero+1):
            suma = suma + i
        print(f"La suma de todos los numeros desde 0 hasta {numero} es {suma}")
        break
    else:
        print("El numero debe de ser mayor a 0 no menor o igual. Vuelva a intentar")

#Ejercicio 8:
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(1,101):
    numero = int(input("Ingrese un numero "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    if numero >= 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1

print (f"En total se ingresaron {pares} numeros pares, {impares} numeros impares, {positivos} numeros positivos y {negativos} numeros negativos")

#Ejercicio 9:
total = 100
resultado = 0
for i in range(1,total + 1):
    numero = int(input("Ingrese un numero "))
    resultado = resultado + numero
resultado = resultado / total
print(f"La media de los {total} numeros ingresados es: {resultado}")

#Ejercicio 10:
numero = int(input("Ingrese un numero "))
aux = numero
cifra = 0
numeroInvertido = ""
while aux > 0:
    cifra = aux % 10
    aux = math.trunc(aux / 10)
    numeroInvertido = numeroInvertido + str(cifra)
int(numeroInvertido)
print(f"El numero {numero} invertido quedaria asi: {numeroInvertido}")