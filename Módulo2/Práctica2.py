## LISTAS
fechas=["12-01-2023","11-01-2023","10-01-2023","11-01-2023","11-01-2023"]
productos=["Producto_A","Producto_AX","Producto_D","Producto_C","Producto_B"]
cantidades=[50,160,20,10,1200]
precios=[45,12,15,140,1]
promociones=[True,False,False,False,True]

## Diccionario
ventas={"fecha":fechas,"producto":productos,"cantidad":cantidades,"precio":precios,"promocion":promociones}

### MENÚ
print(""" Hola, Bienvenido al menu de ventas
      Elige la opción que desea realizar
      1. Mostrar el listado de ventas
      2. Añadir un producto
      3. Calcular la suma total de las ventas
      4. Calcular el promedio de ventas
      5. Mostrar el producto con más unidades vendidas
      6. Mostrar el listado de productos""")

opcion=int(input("Ingrese la opción que desea realizar: "))

match opcion:
    case 1:
        print(ventas)
        
    case 2:
        print(ventas["producto"])
        producto_elegido = int(input("elige el producto que desea añadir: "))
        
    case 3:
        print(precios,cantidades)
        ventastotales=list(map(lambda x,y: x*y, precios, cantidades))
        suma=sum(ventastotales)
        print("El valor de las ventas totales es ",suma)
    
    case 4:
        print(precios,cantidades)
        ventastotales=list(map(lambda x,y: x*y, precios, cantidades))
        suma=sum(ventastotales)
        print(f"El promedio de las ventas es igual a {suma/len(ventastotales)}")

    case 5:
        pro=productos[-1]
        maximo=max(cantidades)
        print(f"El producto con más unidades vendidaes es {pro} con {maximo} unidades")

    case 6:
        print(productos)

    case default:
        print("Comando desconocido")