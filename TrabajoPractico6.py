#Actividad 1
#Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#Actividad 2
#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Ingrese su nombre ")
saludar_usuario(nombre)

#Actividad 3
#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def infomacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
while True:
    try:
        edad = int(input("Ingrese su edad "))
        break
    except ValueError:
        print("Error, vuelva a intentar")
residencia = input("Ingrese su residencia ")
infomacion_personal(nombre,apellido,edad,residencia)

#Actividad 4
#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
# devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio 
# como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y 
# llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    area = 3.1416 * radio ** 2 
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * radio * 3.1416
    return perimetro

while True:
    try:
        radio = float(input("Ingrese el radio de un circulo "))
        break
    except ValueError:
        print("Error no ingreso un numero, vuelva a intentar")
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El area y perimetro de un circulo con radio {radio} es: {area} y {perimetro}")

#Actividad 5
#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos/3600
    return horas

while True:
    try:
        segundos = int(input("Ingrese un cantidad de segundos "))
        break
    except ValueError:
        print("Error, no ingreso los segundos correctamente")
hora = segundos_a_horas(segundos)
print(f"Los segundos {segundos} equivalen a {hora} horas")

#Actividad 6
#Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(0,10):
        multiplicacion = i * numero
        print(f"{i} x {numero} = {multiplicacion}")

while True:
    try:
        numero = int(input("Ingrese un numero y se mostrara su tabla de multiplicar "))
        break
    except ValueError:
        print("Error no ingreso el numero correctamente")
tabla_multiplicar(numero)

#Actividad 7
#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de 
# sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b == 0:
        division = "No se puede dividir por 0"
    else:
        division = a/b
    tupla = (suma, resta, multiplicacion, division)
    return tupla

while True:
    try:
        numero1 = float(input("Ingrese un primer numero "))
    except ValueError:
        print("Error, vuelva a ingresar un numero")
    try:
        numero2 = float(input("Ingrese un segundo numero "))
        break
    except ValueError:
        print("Error, vuelva a ingresar un numero")
tupla = operaciones_basicas(numero1,numero2)
print(f"La suma, resta, multiplicacion y division entre {numero1} y {numero2} es: {tupla}")

#Actividad 8
#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso/altura ** 2
    return imc

while True:
    try:
        peso = float(input("Ingrese su peso en kg "))
    except ValueError:
        print("Error, vuelva a ingresar su peso")
    try:
        altura = float(input("Ingrese su altura en metros "))
        break
    except ValueError:
        print("Error, vuelva a ingresar su altura")
imc = calcular_imc(peso,altura)
print(f"Su IMC es {imc:.2f}")

#Actividad 9
#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheir(celsius):
    fahrenheir = (celsius * 9/5) + 32
    return fahrenheir

while True:
    try:
        celsius = int(input("Ingrese la temperatura en grados celsius "))
        break
    except ValueError:
        print("Error, vuelva a ingresar la temperatura")
fahrenheir = celsius_a_fahrenheir(celsius)
print(f"{celsius} grados celsius equivalen a {fahrenheir} grados fahrenheir")

#Actividad 10
#Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def cargar_numero():
    while True:
        try:
            n = int(input())
            return n
        except ValueError:
            print("Error no ingreso el numero correctamente")

def calcular_promedio(a, b, c):
    promedio = (a + b + c)/3
    print(f"El promedio de los numeros {a}, {b} y {c} es {promedio}")

print(f"Ingrese el primer numero")
numero1 = cargar_numero()
print(f"Ingrese el segundo numero")
numero2 = cargar_numero()
print(f"Ingrese el tercer numero")
numero3 = cargar_numero()
calcular_promedio(numero1,numero2,numero3)