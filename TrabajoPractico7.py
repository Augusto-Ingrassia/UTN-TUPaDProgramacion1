#Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
for i,j in precios_frutas.items():
    print(i,":",j)

#Actividad 2
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
for i,j in precios_frutas.items():
    print(i,":",j)

#Actividad 3
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}
frutas = [precios_frutas.keys()]
print(frutas)

#Actividad 4
contactos = {}
for i in range(5):
    contacto = input("Ingrese el nombre del contacto ")
    telefono = int(input("Ingrese el numero del contacto "))
    contactos[contacto] = telefono
for i,j in contactos.items():
    print(i,":",j)

#Actividad 5
frase = input("Ingrese un frase ")
lista = frase.split()
palabras = {}
for i in lista:
    if i in palabras:
        palabras[i] += 1
    else:
        palabras[i] = 1
set = set(lista)
print(f"Lista de las palabras unicas: {set}")
print(f"Lista de las veces que se repiten las palabras: {palabras}")

#Actividad 6
alumno = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno ")
    notas = []
    bandera = 0
    while True:
        try:
            numero = int(input("Ingrese una de las notas del alumno "))
            if 0 <= numero <= 10:
                notas.append(numero)
                bandera += 1
                if bandera == 3:
                    break
            else:
                print("Error, la nota debe de ser entre 0 y 10")
        except:
            print("Error, ingrese un numero")
    alumno[nombre] = tuple(notas)
for i,j in alumno.items():
    print(i,":",j)
    suma = 0
    for n in j:
        suma += n
    promedio = suma/len(notas)
    print(f"El promedio de {i} es: {promedio}")

#Actividad 7
aprobadosP1 = {113,103,110,104,109,114,118,119,112}
aprobadosP2 = {113,104,117,103,120,115,100,102,106}
ambosApr = aprobadosP1 & aprobadosP2
print(f"Estos alumnos aprobaron ambos parciales: {ambosApr}")
unoApr = aprobadosP1 ^ aprobadosP2
print(f"Estos alumnos aprobaron uno de los dos parciales: {unoApr}")
aprobados = aprobadosP1.union(aprobadosP2)
print(f"Esta es la lista total de todos los alumnos aprobados {aprobados}")

#Actividad 8
productos = {"manzana" : 10, "pera" : 5, "banana" : 20}
while True:
    try:
        opcion = int(input("Bienvenido, que desea hacer:\n 1) Consultar el stock de un producto\n 2) Agregar stock a un producto \n 3) Agregar un producto \n 4) Salir \n"))
        if opcion == 1:
            produc = input("Ingrese el nombre del producto ").lower()
            encontrado = False
            for i,j in productos.items():
                if i == produc:
                    print(f"El stock actual del producto {i} es: {j}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"El producto {produc} no se encuentra en la lista")
        elif opcion == 2:
            produc = input("Ingrese el nombre del producto ").lower()
            encontrado = False
            for i,j in productos.items():
                if i == produc:
                    try:
                        stock = int(input(f"Cuanto stock desea agregar al producto {produc} "))
                        if stock > 0:
                            productos[produc] += stock
                        else:
                            print("No se puede poner producto negativo")
                    except:
                        print("Ingrese un numero no una letra")
                    encontrado = True
                    break
            if not encontrado:
                print(f"El producto {produc} no se encuentra en la lista")
        elif opcion == 3:
            produc = input("Ingrese el nombre del producto que desea agregar ").lower()
            encontrado = False
            for i,j in productos.items():
                if i == produc:
                    print(f"El producto {i} ya existe en la lista")
                    encontrado = True
                    break
            if not encontrado:
                while True:
                    try:
                        stock = int(input("Ingrese el stock del nuevo producto "))
                        if stock > 0:
                            productos[produc] = stock
                            break
                        else:
                            print("No puede ingresar stock negativo, vuelva a intentar")
                    except:
                        print("Error, ingrese numeros enteros")
        elif opcion == 4:
            print("Hasta luego")
            break
        else:
            print("Error, opcion no disponible vuelva a intentar")
    except:
        print("Error, ingrese el numero de la operacion que desea realizar")

#Actividad 9
agenda = {("lunes", "8:00") : "Clase de Matematicas", ("lunes", "18:00") : "Cumple Lola",
          ("martes", "8:00") : "Clase de Organizacion Empresarial", ("martes", "15:00") : "Gimnasio",
          ("miercoles", "8:00") : "Clase de Arquitectura y Sistemas operativos", ("miercoles", "19:00") : "Salida al cine",
          ("jueves", "8:00") : "Clase de Programacion", ("jueves", "20:00") : "Practica Ingles",
          ("viernes", "8:00") : "Clase de Ingles", ("viernes", "14:00") : "Almuezo familiar",
          ("sabado", "8:00") : "Horas Libres", ("sabado", "17:00") : "Juntada de amigos",
          ("domingo", "8:00") : "Horas Libres", ("domingo", "16:00") : "Cumpleaños Tia Stela"}
lista = ["lunes","marte","miercoles","jueves","viernes","sabado","domingo"]
dia = input("Ingrese el dia de la semana ").lower()
if dia in lista:
    hora = input("Ingrese la hora del dia ")
    fecha = (dia,hora)
    if fecha in agenda:
        print(f"El dia {dia} a las {hora} hay programado: {agenda[fecha]}")
    else:
        print(f"El dia {dia} a las {hora} no hay nada programado")
else:
    print("No existe el dia ingresado")

#Actividad 10
diccionario = {"Argentina" : "Buenos Aires", "Brasil" : "Brasilia", "Chile" : "Santiago de Chile", "Estados Unidos" : "Washintong D.C.", "España" : "Madrid", "Francia" : "Paris", "Japon" : "Tokio"}
diccionarioInvertido = {}
print("Esta es la lista de los paises con sus capitales:")
for i,j in diccionario.items():
    print(i,":",j)
    diccionarioInvertido[j] = i
print("Y este es la misma lista pero invertida")
for i,j in diccionarioInvertido.items():
    print(i,":",j)