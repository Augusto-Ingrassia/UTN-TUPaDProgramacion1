print("Sobre escribiendo productos.txt")
productos = []
with open("productos.txt","r") as producto:
    for linea in producto:
        lista = linea.strip().split(",")
        diccionario = {"nombre":lista[0],"precio":lista[1],"cantidad":lista[2]}
        productos.append(diccionario)

with open("productos.txt","w") as archivo:
    for i in productos:
        archivo.write(f"{i["nombre"]},{i["precio"]},{i["cantidad"]}\n")