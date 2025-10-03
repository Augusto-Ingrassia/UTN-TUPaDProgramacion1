print("Leyendo el archivo productos.txt")
with open("productos.txt","r") as produtos:
    for linea in produtos:
        linea = linea.strip()
        lista = linea.split(",")
        print(f"Productos: {lista[0]} | Precio: ${lista[1]} | Cantidad: {lista[2]}")