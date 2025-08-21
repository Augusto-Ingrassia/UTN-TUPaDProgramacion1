# Actividad 1
print("Hola Mundo!")

# Actividad 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Actividad 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Actividad 4
radio = float(input("Ingrese el radio de un circulo: "))
area = 3.1416 * radio**2
perimetro = 2*3.1416*radio
print(f"El area del perimetro es {area} y su perimetro es {perimetro}")

# Actividad 5
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

# Actividad 6
numero = int(input("Ingrese un numero: "))
print(f"{numero} x 0 = {numero * 0}")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# Actividad 7
numero1 = float(input("Ingrese un numero distinto de 0: "))
numero2 = float(input("Ingrese otro numero distinto de 0: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1*numero2
division = numero1/numero2
print(f"La suma de los numeros {numero1} y {numero2} es: {suma}")
print(f"La resta de los numeros {numero1} y {numero2} es: {resta}")
print(f"La multiplicacion de los numeros {numero1} y {numero2} es: {multiplicacion}")
print(f"La division de los numeros {numero1} y {numero2} es: {division}")

# Actividad 8
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = round(peso / altura**2)
print(f"Su IMC (Indice de masa corporal) teniendo en cuenta su peso en kilogramos {peso} y su altura en metros {altura} es de {imc}")

# Actividad 9
celsius = int(input("Ingrese la temperatura en grados celsius: "))
fahrenheit = 9/5 * celsius + 32
print(f"La tempresatura {celsius} en grados celsius es equivalente a {fahrenheit} en grados fahrenheit")

# Actividad 10
numero1 = float(input("Ingrese un primer numero: "))
numero2 = float(input("Ingrese un segundo numero: "))
numero3 = float(input("Ingrese un tercer numero: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los tres numeros ingresados ({numero1}, {numero2}, {numero3}) es: {promedio}")