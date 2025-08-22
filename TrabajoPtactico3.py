#Actividad 1:
edad = int(input("Ingrese su edad en numeros "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#Actividad 2:
nota = int(input("Ingrese la nota que saco en el examen "))
if nota >= 6 and nota <= 10:
    print("Aprobado")
elif nota >= 0 and nota < 6:
    print("Desaprobado")
else:
    print("No puede sacarse una nota mayor a 10 o menor a 0")

#Actividad 3:
numero = int(input("Ingrese un numero par "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Actividad 4:
edad = int(input("Ingrese su edad en numeros "))
if edad < 12:
    print("Eres un niño o niña")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente")
elif edad >= 18 and edad < 30:
    print("Eres un adulto joven")
else:
    print("Eres un adulto")

#Actividad 5:
contrasena = input("Ingrese una contraseña de entre 8 a 14 caracteres ")
longitud_contrasena = len(contrasena)
if longitud_contrasena >= 8 and longitud_contrasena <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6:
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(100)]
media = mean(numeros_aleatorios)
mediana = median (numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Lista de numeros: ",numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
if  media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

#Actividad 7:
vocales = "aeiou"
frase = input("Ingrese una frase o palabra ")
letra = frase[-1].lower()
if letra in vocales:
    print(frase + "!")
else:
    print(frase)

#Actividad 8:
nombre = input("Ingrese su nombre ")
numero = int(input("Ingrese un numero 1 si quiere su nombre en mayusculas, el numero 2 si lo quiere en minusculas o el numero 3 si quiere la primer letra en mayusculas "))
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("No existe niguna opcion con ese numero, vuelva a intentar")

#Actividad 9:
magnitud = int(input("Ingrese la magnitud del terremoto "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptivo)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por persona, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daño en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#Actividad 10:
hemisferio = input("Ingrese a que hemisferio pertenece (norte o sur) ").lower()
mes = int(input("Ingrese en que mes del año se encuentra (1-12) "))
dia = int(input("Ingrese el dia en el que se encuentra "))
if hemisferio == "norte":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <=20):
        print("Usted se encunetra en Invierno")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <=20):
        print("Usted se encunetra en Primavera")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <=20):
        print("Usted se encunetra en Verano")
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <=20):
        print("Usted se encunetra en Otoño")
    else:
        print("Mes o dia incorrectos, vuelva a intentar")
elif hemisferio.lower() == "sur":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <=20):
        print("Usted se encunetra en Verano")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <=20):
        print("Usted se encunetra en Otoño")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <=20):
        print("Usted se encunetra en Invierno")
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <=20):
        print("Usted se encunetra en Primavrea")
    else:
        print("Mes o dia incorrectos, vuelva a intentar")
else:
    print("Error, hemisferio equivocado")