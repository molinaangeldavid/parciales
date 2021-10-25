# 4) Una importante empresa de cosmética nos solicita realizar un programa para la automatización de su producción
# de cremas.
# La línea de producción consta de 5 tipos de cremas (Humectante clásica {cod.100}, Antiage colageno {cod.200}, Facial
# con UV {cod.300}, Desmaquillante{cod.400}, Vitamina A {cod. 10}) y 3 envases (200 cm3, 500cm3 y 1000 cm3).
# El usuario comenzará introduciendo la cantidad de cm3 de cada tipo de crema disponible en la fábrica (estos están
# almacenados en 5 grandes tanques cisternas).
# Posteriormente el sistema le solicitará al usuario:
# - Ingresar la crema para ser utilizados en la línea de producción (se debe ingresar por código), por una
# cuestión de evitar contaminación en la línea de producción, sólo se podrá procesar una crema a la vez.
# - Cantidad y tipo de envases a utilizar por cada crema
# El sistema deberá determinar si alcanza la cantidad de materia prima (cremas) en cada tanque para procesar lo pedido
# por el usuario
# a) en el caso que NO se pueda, deberá solicitar nuevamente que se ingresen los datos
# b) en caso que SI se pueda, deberá indicar:
#  Cuál fue la crema que más se produjo (mostrar código y nombre de la crema)
#  Cuál es el envase que más se produjo sobre el total de tipos de cremas
#  Y el sobrante en cada tanque por tipo de crema
# Obs.
# - El programa deberá tener al menos 2 funciones.
# - Se deberá contemplar alguna estructura que permita guardar el código de color y el nombre
CREMAS = {
        100: 'Humectante clásica',
        200: 'Antiage colageno',
        300: 'Facial con UV',
        400: 'Desmaquillante',
        10: 'Vitamina A'
    }

def validar_cantidad_cremas()->int:
    '''
    PRE:---
    POST: Retorna un valor numerico entero, la cual es la cantidad de crema que habra en la cisterna
    '''
    cantidad_cremas = input(f'Ingrese la cantidad en cm3: ')
    while not (cantidad_cremas.isnumeric() and int(cantidad_cremas)<=10000):
        cantidad_cremas = input(f'Error!! Ingrese la cantidad en cm3 <0-10000cm3>: ')
    cantidad_cremas = int(cantidad_cremas)
    return cantidad_cremas

def menu_envases()->int:
    '''
    PRE:---
    POST: Retorna un valor numerico entero, la cual es el envase que se utilizara en la produccion
    '''
    print('1.Producir envase 200cm3')
    print('2.Producir envase 500cm3')
    print('3.Producir envase 1000cm3')
    elegir_envase = int(input('Ingresar el envase a utilizar: <1,2,3>: '))
    return elegir_envase   

def cisternas()->dict:
    '''
    PRE:---
    POST: Retorna un diccinario, la cual son la cantidad de cremas que hay en cada cisterna
    '''
    cisternas_cantidad_cremas = {} 
    for key in CREMAS.keys():
        print(f'Ingresa la cantidad de {CREMAS[key]} en la cisterna')
        cantidad_cremas = validar_cantidad_cremas()
        cisternas_cantidad_cremas[key] = cantidad_cremas
    return cisternas_cantidad_cremas

def cargar_datos()->tuple:
    '''
    PRE:---
    POST: Retorna dos diccionarios, uno que indica la cantidad de envases utilizados y otra que indica el codigo de la crema y cantidad en la cisterna
    '''
    lista_cisterna = []
    lista_envases = []
    crema_produccion = {}
    init = False
    while not init:
        cisternas_cantidad_cremas = cisternas() # {100: cantidad crema,200: cantidad crema,...}
        for crema in cisternas_cantidad_cremas.keys():
            contador_envase_200 = 0
            contador_envase_500 = 0
            contador_envase_1000 = 0
            print(f'Producir crema {CREMAS[crema]}')
            crem = cisternas_cantidad_cremas.get(crema)
            while crem > 200:
                print(f'Cantidad de crema en cisterna <{cisternas_cantidad_cremas.get(crema)}>')
                print('Indique que envase utilizará: ')
                envase = menu_envases()
                if envase == 1:
                    cisternas_cantidad_cremas[crema] -= 200
                    crem = cisternas_cantidad_cremas.get(crema)
                    contador_envase_200 += 1
                    if crem < 1000:
                        print('\t-----Hay muy poca materia prima en la cisterna-----')
                        print(f' En total hay {crem} de {CREMAS.get(crema)}')
                elif envase == 2:
                    cisternas_cantidad_cremas[crema] -= 500
                    crem = cisternas_cantidad_cremas.get(crema)
                    contador_envase_500 += 1    
                    if crem < 1000:
                        print('\t------Hay muy poca materia prima en la cisterna------')
                        print(f' En total hay {crem} de {CREMAS.get(crema)}')
                elif envase == 3:
                    cisternas_cantidad_cremas[crema] -= 1000
                    crem = cisternas_cantidad_cremas.get(crema)
                    contador_envase_1000 += 1   
                    if crem < 1500:
                        print('\t------Hay muy poca materia prima en la cisterna------')
                        print(f' En total hay {crem} de {CREMAS.get(crema)}')
            crema_produccion[crema] = [contador_envase_200,contador_envase_500,contador_envase_1000]          
            lista_cisterna.append(crem)
            if len(lista_envases)==0:
                lista_envases.append(contador_envase_200) 
                lista_envases.append(contador_envase_500) 
                lista_envases.append(contador_envase_1000) 
            else:
                lista_envases[0] += contador_envase_200     
                lista_envases[1] += contador_envase_500     
                lista_envases[2] += contador_envase_1000     
        cantidad = [values for values in cisternas_cantidad_cremas.values()]
        print(cantidad)
        if min(cantidad)<0:
            print('Ha sobrepasado la produccion con la materia prima faltante... Vuelva a intentar')
            init = False
        elif min(cantidad)>0:
            print('\t\tGuardando datos de produccion...')
            init = True
    cisternas_cantidad_cremas                   
    return lista_envases,crema_produccion,cisternas_cantidad_cremas

def mayor_crema(produccion)->None: #crema_produccion {100: [4,3,1], 200:[8,4,2],...}
    lista_producciones = []
    for key in produccion.keys():
        envases_totales = sum(produccion.get(key))
        lista_producciones.append(envases_totales)
        
        if max(lista_producciones) == sum(produccion.get(key)):
            return (f'La crema mas producida fue {key}:{CREMAS[key]}')        

def envases(produccion)->None:
    envase_mas_producido = max(produccion)
    if envase_mas_producido == produccion[0]:
        return (f'El envase mas producido es de 200cm3, la cual en total son {envase_mas_producido}')
    elif envase_mas_producido == produccion[1]:
        return (f'El envase mas producido es de 200cm3, la cual en total son {envase_mas_producido}')
    elif envase_mas_producido == produccion[2]:
        return (f'El envase mas producido es de 200cm3, la cual en total son {envase_mas_producido}')    

def sobrantes(produccion)->None: #cisternas_cantidad_cremas
    for key in produccion:
        print(f'En la cisterna de {CREMAS.get(key)} sobra {produccion.get(key)}')

def main ()->None:
    output = {}
    init = False
    while not init:
        print('1.Cargar datos')
        print('2.Salir')
        opcion = int(input('Ingrese una opcion para proseguir: '))
        if opcion == 1:
            produccion = cargar_datos()
            init2 = False
            while not init2:
                print('1.Crema que mas se produjo')
                print('2.Envase que mas se utilizó')
                print('3.Sobrante en cada cisterna')
                print('4.Atras')
                opcion = int(input('Ingrese una opcion para proseguir: '))
                if opcion == 1:
                    print(mayor_crema(produccion[1]))
                elif opcion == 2:
                    print(envases(produccion[0]))
                elif opcion == 3:
                    sobrantes(produccion[2])
                elif opcion == 4:
                    init2 = True    
        elif opcion == 2:
            init = True
main()    

