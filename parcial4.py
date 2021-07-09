#--------------------Ejercicio 1--------------------------------
# 1) (Obligatorio tener 1 pto bien)
# a- Pasar el siguiente número en base 10 a base 9 con error menor o igual a 10-4:
# 858,21
#--------------------Ejercicio2 --------------------------------
# b- Pasar el siguiente número de base 8 a base 16 y justifique el método por el cual decidió hacer la
# conversión:
# 4447,601
#--------------------Ejercicio 3 ---------------------------------------------
# 2)Nos contratan de una empresa textil fabricante de hilado y telas de algodón para la creación de un simple software
# que permita la carga de pedidos.
# El sistema deberá permitir la carga de un nuevo pedido o la modificación de un pedido ya existente, como así
# también la carga de un nuevo stock, o la modificación de uno existente.
# Para el stock de sus productos la empresa cuenta con esta información: Número de Artículo, Descripción, color,
# cantidad, precio
# Para tomar un pedido la empresa necesita esta información: Nro de cuenta, Razón Social, artículos, color, cantidades
# pedidas, total valorizado del pedido.
# Ejemplo de datos:
# Para el stock
# 271, rebb 100% algodón peinado, Crudo, 1500kg, 825$/Kg
# 271, rebb 100% algodón peinado, Negro, 150kg, 980$/Kg
# 271, rebb 100% algodón peinado, Azul Marino, 500kg, 980$/Kg
# 271, rebb 100% algodón peinado, Blanco, 100kg, 825$/Kg
# 433, jersey 100% algodón peinado, Rosa, 300kg, 788$/Kg
# 433, jersey 100% algodón peinado, Blanco, 30kg, 788$/Kg
# …
# El sistema debe tener:
# Un pequeño menú que permita :
# a- La carga o modificación de un pedido (Un pedido puede estar compuesto por más de un artículo)
# b- La carga o modificación de un stock existente
# c- Listar los pedidos de un nro de cuenta o Razón Social dada
# d- Mostrar el pedido cuya valorización sea la mayor
# e- Listar todos los pedidos cargados.
#----------------------Ejercicio 4--------------------------
# La Pizzería "La Casa de Matias" nos solicita generar un sistema que permita ingresar y calcular el importe a abonar por un cliente y a su vez tener un control total de todo lo vendido.
# La Pizzería trabaja con 3 productos diferentes:
# 1.	Pizza de Muzzarella
# 2.	Pizza de Fugazzetta
# 3.	Pizza Napolitana
# El cliente debe ir indicando que producto desea y que cantidad de este.El sistema debe controlar que solamente se pueda pedir alguna variedad dentro de las 3 que vende el local. El cliente puede, en el mismo pedido, volver a pedir un producto que ya pidió.El sistema deberá indicar al finalizar el pedido, un detalle de la cantidad y de los importes parciales de cada uno de los ítems, y finalmente el precio total del pedido.
# La pizzería tiene una promoción que para pedidos superiores a $500, otorga un 10% de descuento sobre el total de la compra.
# Luego del último pedido del día, el sistema deberá informar cual fue la facturación del día y cuál fue elNº de pedido en el cual se produjo la venta mas grande, indicando su importe.
# Nota: Los importes unitarios de cada uno de los productos deben ser definidos como constantes en el programa, a gusto de cada uno de los programadores.
# Nota 2: El sistema NO debe preguntar al cliente cuanto quiere de cada artículo, sino que el usuario debe indicar que quiere pedir y cuánto.
PIZZAS = {
    1: ['Muzzarella vegana', 240],
    2: ['Fugazzetta vegana', 200],
    3: ['Napolitana vegana', 330]
}
def validar_opcion()->str:
    opcion = input('Ingrese si o no: ')
    while not (opcion.isalpha() and opcion == 'si' or opcion == 'no'):
        opcion = input('Error de ingreso. Vuelva a ingresar: ')
    return opcion

def validar_pedido()->int:
    pedido = input('Ingrese que pizza desea: ')
    while not (pedido.isnumeric() and int(pedido)>=1 and int(pedido)<=3):
        pedido = input('Ingresaste una opcion incorrecta. Vuelva a intentarlo: ')
    pedido = int(pedido)
    return pedido    

def facturacion(pedido_dia)->tuple:
    total_del_dia = 0
    for values in pedido_dia.values():
        total_del_dia += values[1]

    return total_del_dia    

def descuento(precio_total:int)->float:
    if precio_total > 500:
        precio_reducido = (precio_total * 10) / 100
    return precio_reducido     

def ticket(pedido:list,contador_cliente:int)->list: #pedido es [[3,240],[1,400],[3,500]]
    precios = []
    nombre_pizza = []
    precio_total = 0
    pedido_cliente = {1:0,2:0,3:0}
    numero_cliente = contador_cliente
    for values in PIZZAS.values():
        precios.append(values[1])
        nombre_pizza.append(values[0])
    for cada_pedido in pedido:
        for key in pedido_cliente.keys():
            if cada_pedido[0] == key:
                suma = pedido_cliente.get(key)
                suma += cada_pedido[1]
                pedido_cliente[key] = suma
    for key,values in pedido_cliente.items():
        if key == 1:
            resultado1 = values / precios[0]
        elif key == 2:
            resultado2 = values / precios[1]    
        elif key == 3:
            resultado3 = values / precios[2] 
    if precio_total >500:
        precio_total = descuento(precio_total)
    print(f'''\tN° de cliente: {numero_cliente}
        {resultado1} : {nombre_pizza[0]}...........{pedido_cliente.get(1)}
        {resultado2} : {nombre_pizza[1]}...........{pedido_cliente.get(2)}
        {resultado3} : {nombre_pizza[2]}...........{pedido_cliente.get(3)}

                                                Total = {precio_total}''')     

def pedir_pedido()->None:
    pedidos_clientes = {} # { 1: [[3,precio],[1,precio]], 2: [[1,precio],[3,precio]]}
    contador_cliente = 0
    init_pedido = False
    while not init_pedido:
        print('Desea cerrar la pizzeria')
        cerrar_pizzeria = validar_opcion()
        if cerrar_pizzeria == 'si':
            init_pedido = True
            return pedidos_clientes
        else:
            contador_cliente += 1
            p = [] #[[3,1],[1,1]]
            init_cliente = False
            while not init_cliente:
                print('\t-- Bienvenido a pizzana --')
                print('1. Pizza muzzarella vegana -> $240')
                print('2. Pizza Fugazzeta vegana -> $200')
                print('3. Pizza Napolitana vegana -> $330\n')
                pedido = validar_pedido()
                cantidad_pedido = int(input('Ingrese cantidad: '))
                print('Desea seguir pidiendo?')
                continuar = validar_opcion()
                if continuar == 'si': #condicion continuar pedido
                    precio = PIZZAS.get(pedido)
                    total = cantidad_pedido*precio[1]
                    p.append([pedido,total])
                elif continuar == 'no': #condicion finalizar pedido
                    init_cliente = True
                    precio = PIZZAS.get(pedido)
                    total = cantidad_pedido*precio[1]
                    p.append([pedido,total])
                    pedidos_clientes[contador_cliente] = [p]   
                    ticket(p,contador_cliente)

def main():
    todos_los_pedidos = pedir_pedido()
    print(facturacion(todos_los_pedidos))
main()    