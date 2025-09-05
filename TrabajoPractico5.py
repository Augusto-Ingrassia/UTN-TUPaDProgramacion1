#Actividad 1
#Primera forma de resolverlo
lista = list(range(4,101,4))
print(lista)

#Segunda forma de resolverlo
Lista2 = []
for i in range(4,101,4):
    Lista2.append(i)
print(Lista2)

#Tercera forma de resolverlo
lista3 = []
for i in range(1,101):
    if i % 4 == 0:
        lista3.append(i)
print(lista3)

#Actividad 2
lista = []
for i in range(5):
    lista.append(input("Ingrese cualquier cosa "))
print(f"Esta es la lista completa: {lista}")
print(f"Este es el ultimo valor de la lista: {lista[4]}")

#Actividad 3
lista = []
for i in range(3):
    lista.append(input("Ingrese cualquier cosa "))
print(f"Esta es la lista: {lista}")

#Actividad 4
#forma 1
lista = ["Perro","Gato","Conejo","Pez"]
lista[1] = "Loro"
lista[3] = "Oso"
print(lista)

#forma 2
lista = ["Perro","Gato","Conejo","Pez"]
for i in range(len(lista)):
    if i == 1:
        lista[i] = "Loro"
    elif i == len(lista)-1:
        lista[i] = "Oso"
print(lista)

#Actividad 5
#El siguiente programa:
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
#Lo que hace es remover o quitar el numero mas grande dentro de la lista 

#Actividad 6
lista = list(range(10,31,5))
for i in range(2):
    print(lista[i])

#Actividad 7:
autos = ["sedan", "polo", "suran", "gol"]
print(f"Esta es la lista original: {autos}")
autos[1] = input("Ingrese cualquier cosa ")
autos[2] = input("Ingrese cualquier cosa ")
print(f"Esta es la nueva lista: {autos}")

#Actividad 8:
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#Actividad 9:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("Jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#Actividad 10:
lista_anidad = [15,True,[25.5,57.9,30.6],False]
print(lista_anidad)