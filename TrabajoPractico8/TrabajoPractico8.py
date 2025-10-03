#En este archivo se encuentra la convinacion de las 6 actividades anteriores aplicadas en un solo archivo como conjunto, algunas partes
#se tuvieron que cambiar (como el append del punto 3) ya que se supepnian con otras que cumplian esa misma funcion (del caso del punto 3
# hace exactamente lo mismo que el punto 6)

#Actividad 3
def agregarProducto(existente,productos):
    while True:
        producto = input("Ingrese el nombre del producto que desea agregar ")
        if producto.lower() in existentes:
            print("Error el producto ya existe")
        else:
            print("Ingrese el precio del producto")
            precio = validarValores()
            print("Ingrese la cantidad del producto")
            cantidad = validarValores()
            diccionario = {"nombre":producto,"precio":precio,"cantidad":cantidad}
            productos.append(diccionario)
            break

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

#Actividad 5
def buscarProducto(productos):
    nombre = input("Ingrese el nombre del producto que desea buscar ")
    for i in productos:
        if nombre.lower() == i["nombre"].lower():
            print("Producto encontrado")
            print(i)
            break
    else:
        print("Producto no encontrado o no valido, vuelva a intentar")

#Activida 1
print("Escribiendo archivo productos.txt")
archivoProducto = open("productos.txt","w")
archivoProducto.write("Lapiz,30,200\n")
archivoProducto.write("Goma,10,500\n")
archivoProducto.write("Cuaderno,50,130\n")
archivoProducto.close()

#Actividad 2 con cosas de la activiadad 3 y 4
print("Leyendo el archivo productos.txt")
#Parte de la actividad 3
existentes = []
#Parte de la actividad 4
productos = []
with open("productos.txt","r") as produto:
    for linea in produto:
        lista = linea.strip().split(",")
        print(f"Producto: {lista[0]} | Precio: ${lista[1]} | Cantidad: {lista[2]}")
        #Parte de la actividad 3
        existentes.append(lista[0].lower())
        #Parte de la actividad 4
        diccionario = {"nombre":lista[0],"precio":lista[1],"cantidad":lista[2]}
        productos.append(diccionario)

while True:
    agregarProducto(existentes,productos)
    respuesta = input("Si desea seguir agregando productos ingrese S o Si, en caso contrario ingrese cualquier otra cosa ").lower()
    if respuesta !="s" and respuesta !="si":
        break

#Actividad 4
for i in productos:
    print(i)

while True:
    buscarProducto(productos)
    respuesta = input("Si desea seguir buscando productos ingrese S o Si, en caso contrario ingrese cualquier otra cosa ").lower()
    if respuesta !="s" and respuesta !="si":
        break

#Actividad 6
print("Sobre escribiendo productos.txt")
with open("productos.txt","w") as archivo:
    for i in productos:
        archivo.write(f"{i["nombre"]},{i["precio"]},{i["cantidad"]}\n")