#--------------------------Ejercicio 3---------------------------------
# 3. La fiambrería Los sabores de Ari nos solicita armar un sistema para poder mantener su dinámica de negocio en línea. Sabiendo que contamos con el siguiente inventario de productos (el programador puede modificarlos):
# Producto,Frigorifico,Stock en Kg,Precio/100g
# Jamón cocido,Bocatti,20,189
# Jamón cocido,Rogiano,10,117
# Jamón cocido,Paladini,5,113
# Jamón cocido,Tapalque,12,79
# Salame milán,La Piamontesa,7,118
# Salame milán,Bocatti,3,157
# Salame milán,Paladini,4,121
# Mortadela,Calchaqui,11,82
# Mortadela,Paladini,5,90
# Mortadela,Trozer,3,49
# Crear un sistema que realice las siguientes acciones:
# a)Apertura de Caja: Se da por comenzado un nuevo día de trabajo y las compras comienzan de cero para ese día. No puede haber una apertura de caja si aún no está cerrada la del díaanterior.
# b)Nueva Compra: Para poder realizar una compra, la caja tiene que estar abierta. El sistema debe ofrecer un menú para que el cliente elija que productos tiene disponibles, y al seleccionar uno se debe registrar Producto-Frigorifico y Cantidad en gramos solicitada. El cliente puede solicitar varios productos. Ante cada producto solicitado debe controlar que exista stock en línea disponible para cumplir con dicho pedido. Al finalizar la compra se debe imprimir el monto total de la misma.
# c)Reporte Producto  Más  Comprado: En base a todas las compras registradas en el sistema se debe obtener un ranking de producto-frigorífico-kg comprados ordenado descendentemente por kg. comprados.
# d)Reporte Stock por Frigorífico: Debe listar todos los productos de un determinado frigorífico ordenado por precio x 100 grs. de forma ascendente. El sistema debe sugerirle los posibles frigoríficos al usuario.
# e)Cierre  de  Caja: Al cerrar la caja, se calcula cuanto fue el importe total de las ventas del día, se lo muestra por pantalla y se consolida la información para su uso posterior en reportes y pronósticos. Para que pueda realizarse un cierre de caja, la caja tiene que estar abierta.
# f)Pronóstico de Quiebre de Stock: Suponiendo que cada apertura y cierre de caja seda 1 vez por día, se debe utilizar las cantidades compradas de los productos para estimarel volumen de compra mensual. En caso de tener 2 muestras (2 ciclos de apertura-cierre decaja) se puede suponer que multiplicando por 15 se consigue obtener un estimado mensual.Si tenes 3 muestras, multiplicando por 10 tenes el estimado mensual y así. El multiplicadorse consigue haciendo 30/N, siendo N la cantidad de aperturas y cierres obtenidos. Con elestimado mensual por producto, se desea saber que productos corren riesgo de quebrar stock(quedarse sin stock) en 1 mes. Vale aclarar que las compras del día corriente en el cual aún no fue cerrada la caja deben descartarse.
def apertura_caja(productos:dict)->None: 

    init_caja = False
    while not init_caja:
        print('1.Nueva compra')
        print('2.Cerrar caja')
        opcion = int(input('Ingrese una opcion valida: '))
        if opcion == 1:
            nueva_compra(productos)
        else:
            init_caja = True

def nueva_compra(productos:dict)->None:
    init_cliente = False
    while not init_cliente:
        print('''1.'Jamón cocido','Bocatti'
        2.'Jamón cocido','Rogiano',
        3.'Jamón cocido','Paladini',
        4.'Jamón cocido','Tapalque',
        5.'Salame milán','La Piamontesa',
        6.'Salame milán','Bocatti',
        7.'Salame milán','Paladini',
        8.'Mortadela','Calchaqui',
        9.'Mortadela','Paladini',
        10.'Mortadela','Trozer''')
        producto = int(input('\tIngrese el producto deseado: '))
        cantidad_gramos = int(input('\tIngrese la cantidad en gramos del producto: '))
        print(f'Queda en stock {productos[producto][2]} Kg de {productos[producto][0]},{productos[producto][1]}')
        continuar = input('Ingresar mas pedido: <si/no>: ')
        if continuar == 'si':
            productos[producto][2] -= cantidad_gramos/1000
            productos[producto][4] += cantidad_gramos/1000
        else:
            init_cliente = True
    
def reporte_mas_comprado(productos:dict)->None:
    maximo = 0
    keymaximo=""
    for k,i in productos.items():
        if(i[4]>maximo):
            maximo = i[4]
            keymaximo=k
    print("el mas comprado es",productos[keymaximo])

def stock_frigorifico(productos:dict)->None:
    valores = []
    for value in productos.values():
        valores.append([value[1],value[3]])
    valores.sort()
    return valores

def pronostico_quiebre()->None:
    pass

def opciones()->None:
    productos = { #Producto,Frigorifico,Stock en Kg,Precio/100g
        1:['Jamón cocido','Bocatti',20,189,0],
        2:['Jamón cocido','Rogiano',10,117,0],
        3:['Jamón cocido','Paladini',5,113,5],
        4:['Jamón cocido','Tapalque',12,79,0],
        5:['Salame milán','La Piamontesa',7,118,0],
        6:['Salame milán','Bocatti',3,157,0],
        7:['Salame milán','Paladini',4,121,0],
        8:['Mortadela','Calchaqui',11,82,0],
        9:['Mortadela','Paladini',5,90,0],
        10:['Mortadela','Trozer',3,49,0]
    }

    sort_orders = sorted(productos.items())
    print(sort_orders)

    stock_productos = []
    for value in productos.values():
        stock_productos.append(value[2]*1000)
    init_sistema = False
    while not init_sistema:
        print('1.Apertura de caja')
        print('2.Reporte producto mas comprado')
        print('3.Reporte stock por frigorifico')
        print('4.Pronostico quiebre de stock')
        print('5.Cerrar sistema')
        opcion = int(input('Ingrese una opcion del sistema -Ari-: '))
        if opcion == 1:
            apertura_caja(productos,stock_productos)
        elif opcion == 2:
            reporte_mas_comprado(productos) 
        elif opcion == 3:
            print(stock_frigorifico(productos)) 
        elif opcion == 4:    
            pronostico_quiebre()
        elif opcion == 5:
            init_sistema = True
def main()->None:
    opciones()
main()    
#---------------------------Ejercicio4------------------------------
# Facundo no sabe sumar, así que nos pidió ayuda. Él nos va a ingresar unstringcon la cantidad del producto, seguida de la primera letra en mayúscula de la fruta o verdura que tiró y nosotrosdebemos calcular el total a pagar.Se deberá crear una función que reciba dos parámetros:un diccionario de preciosuna cadena de texto con el detalle de los ítems a contabilizar y devuelva la cuenta total a pagar.Aclaración: No van a haber entradas con más de una unidad. Ejemplo: "3T 5P 2M 6B 2K 10T".Ejemplo:>>>"3T 5P 2M 6B 2K"550


FRUTAS = {
    'Tomate':35,
    'Banana':20,
    'Kiwi':70,
    'Mandarina':30,
    'Pera':25
}

def conversion(FRUTAS:dict,ingreso:str)->int:
    precio_total = 0
    lista_ingreso = ingreso.split() 
    lista2 = [] 
    for i in lista_ingreso: 
        listar_i = list(i) 
        lista2.append(listar_i)
    for key,value in FRUTAS.items(): 
        for str in lista2:
            if str[1] == key[0]:
                cantidad_producto = int(str[0]) * value
                precio_total += cantidad_producto
    return precio_total            

def main()->None:
    ingreso = input('Ingrese cantidad y primera letra de la fruta: ') #3T 2B 5M...
    print(conversion(FRUTAS,ingreso))
main()    