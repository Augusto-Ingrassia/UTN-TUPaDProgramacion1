def validarValores():
    while True:
        try:
            valor = int(input())
            if valor <= 0:
                print("No puede poner valores menores o iguales a 0")
            else:
                return str(valor)
        except:
            print("Debe de ingresar numeros")

print("Leyendo el archivo productos.txt")
existentes = []
with open("productos.txt","r") as productos:
    for linea in productos:
        linea = linea.strip()
        lista = linea.split(",")
        print(f"Productos: {lista[0]} | Precio: ${lista[1]} | Cantidad: {lista[2]}")
        existentes.append(lista[0].lower())

while True:
    producto = input("Ingrese el nombre del producto ")
    if producto.lower() in existentes:
        print("Error el producto ya existe")
    else:
        print("Ingrese el precio del producto")
        precio = validarValores()
        print("Ingrese la cantidad del producto")
        cantidad = validarValores()
        break

with open("productos.txt","a") as productos:
    productos.write(f"{producto},{precio},{cantidad}")
