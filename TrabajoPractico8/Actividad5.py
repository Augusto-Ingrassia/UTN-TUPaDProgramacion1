print("Leyendo el archivo productos.txt")
productos = []
with open("productos.txt","r") as producto:
    for linea in producto:
        lista = linea.strip().split(",")
        diccionario = {"nombre":lista[0],"precio":lista[1],"cantidad":lista[2]}
        productos.append(diccionario)

nombre = input("Ingrese el nombre del producto que desea buscar ")
for i in productos:
    if nombre.lower() == i["nombre"].lower():
        print("Producto encontrado")
        print(i)
        break
else:
    print("Producto no encontrado o no valido, vuelva a intentar")