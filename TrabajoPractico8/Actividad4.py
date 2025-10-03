print("Leyendo el archivo productos.txt")
productos = []
with open("productos.txt","r") as producto:
    for linea in producto:
        lista = linea.strip().split(",")
        diccionario = {"nombre":lista[0],"precio":lista[1],"cantidad":lista[2]}
        productos.append(diccionario)

for i in productos:
    print(i)