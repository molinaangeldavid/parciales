# ----------------------------------------Ejercicio 1 ----------------------------------------------------------------
# 1) Pasar el siguiente número en base 10 a base 6 con error menor o igual a 10-4:
# 1986,0622
# 13110,3422 base 6
#-----------------------------------------Ejercicio 2------------------------------------------------------------------
# 2) Pasar el siguiente número de base 16 a base 4 y justifique el método por el cual decidió hacer la conversión:
# D1E60,D105
# 3101321200,31010011 base 4
#-----------------------------------------Ejercicio 3------------------------------------------------------------------
# 3) Yamila, la cosmetóloga furor en redes, tiene un consultorio donde realiza limpiezas y tratamientos para el cuidado
# de la piel.
# Debido a la alta demanda de sus pacientes y futuros pacientes, nos pidió que realicemos un programa que la ayude
# con la planificación de su negocio. La información del paciente que Yami necesita analizar es la cantidad de consultas
# asistidas y que tratamientos fueron realizados.
# Asimismo, el catálogo de tratamientos que comercializa es el siguiente:
#  - Higiene profunda $1500
#  - Tratamiento Acné $1500
#  - Tratamiento tensor con aparatología $1800
#  - Tratamiento revitalizante $3000
# Hacer un programa que:
#  a) Permita al usuario realizar el ingreso de un paciente. Para ello se solicita:
#  - DNI
#  - Nombre y Apellido
#  - Cantidad de consultas asistidas
#  - Tratamientos realizados (Tipo y cantidad. Puede ser ninguno)
#  b) Emita un reporte que informe el tratamiento más solicitado por los pacientes.
#  c) Emita un reporte que informe el monto total de tratamientos vendidos. ->Hecho
#  d) Emita un reporte que informe el total de pacientes nuevos y viejos. -> Hecho
#  e) Emita un reporte que informe cuál es el tratamiento más solicitado por los pacientes nuevos.
# A tener en cuenta: Se considera que un paciente es *nuevo* en caso de que el mismo haya asistido únicamente a 1
# consulta con el profesional.

TRATAMIENTOS = {
    1: ['Higiene profunda $1500',1500],
    2: ['Tratamiento Acné',1500],
    3: ['Tratamiento tensor con aparatología',1800],
    4: ['Tratamiento revitalizante ',3000],
}

def cantidad_tratamientos(historial:dict)->int: 
    cantidad_tratamientos = 0
    for datos_paciente in historial.values():   
        tratamientos_cantidad = datos_paciente[2]  #historial {dni: [nombre,consultas[tratamiento,cantidad]]}
        for i in tratamientos_cantidad:
            cantidad_tratamientos += i[1]    
    return cantidad_tratamientos   

def extraer_tratamientos(historial)->None: #[[tratamientos,cantidad][tratamientos_nuevos,cantidad]]
    diccionario = {1:0,2:0,3:0,4:0}
    tratamientos = [] # [[1,4],[2,5],[3,5],[2,6]]
    tratamientos_nuevos = []
    diccionario_nuevo = {1:0,2:0,3:0,4:0}
    for datos_paciente in historial.values():
        tratamientos_cantidad = datos_paciente[2]
        if datos_paciente[1] == 1:
            for trat in tratamientos_cantidad:
                tratamientos_nuevos.append(trat)
        for trat in tratamientos_cantidad:
            tratamientos.append(trat)
    for i in tratamientos:
        for key in diccionario:
            if i[0] == key:
                suma = diccionario.get(key)
                suma += i[1]
                diccionario[key] = suma
    for j in tratamientos_nuevos:
        for key2 in diccionario_nuevo:
            if j[0] == key:
                suma2 = diccionario_nuevo.get(key2)
                suma2 += j[1]
                diccionario_nuevo[key2] = suma            
    reporte = mejor_tratamiento(diccionario,diccionario_nuevo)
    return reporte 

def mejor_tratamiento(diccionario,diccionario_nuevo)->None:
    lista_viejos = [] #cantidad de tratamientos
    lista_nuevo = []
    for values in diccionario.values():
        lista_viejos.append(values)
    for values2 in diccionario_nuevo.values():
        lista_nuevo.append(values2)    
    maximo = max(lista_viejos)
    posicion = lista_viejos.count(maximo)
    posicion += 1
    maximo2 = max(lista_nuevo)
    posicion2 = lista_nuevo.count(maximo2)
    posicion2 += 1
    return [posicion,maximo],[posicion2,maximo2]

def main()->None:
    pacientes_nuevos = 0
    pacientes_viejos = 0
    historial = {} 
    init = False
    while not init:
        tratamientos_db = []
        dni = int(input('Ingresa el dni del paciente: '))
        nombre = input('Ingresa el nombre y apellido del paciente: ')
        consultas = int(input('Ingrese la cantidad de consultas que realizo el paciente: '))
        if consultas == 1:
            pacientes_nuevos += 1
        else:
            pacientes_viejos += 1
        init2 = False
        while not init2:   
            print('\t1. Higiene profunda, $1500')
            print('\t2. Tratamiento Acné, $1500')
            print('\t3. Tratamiento tensor con aparatología,$1800')
            print('\t4. Tratamiento revitalizante,$3000')     
            tratamientos = int(input('Ingrese el tipo de tratamiento que realizo: '))
            tratamientos_cantidad = int(input('Cuantos realizo de ese tipo: '))
            tratamientos_db.append([tratamientos,tratamientos_cantidad])
            continuar = int(input('Ingrese 0 si no desea agregar mas tratamientos: '))
            if continuar == 0:
                init2 = True
        historial[dni] = [nombre,consultas,tratamientos_db]        
        continuar2 = int(input('Ingrese 1 si no desea agregar mas pacientes: '))        
        if continuar2 == 1:
            init = True
    print(f'\tLa cantidad de pacientes nuevos son de {pacientes_nuevos}\n')
    print(f'\tLa cantidad de pacientes viejos son en total {pacientes_viejos}\n')
    print(f'En total hay {cantidad_tratamientos(historial)} tratamientos vendidos\t')   
    cant = extraer_tratamientos(historial)
    print(f'\tEl tratamiento mas utilizado es {TRATAMIENTOS.get(cant[0][0])} con {cant[0][1]}\t')
    print(f'\tEl tratamiento mas utilizado por los pacientes nuevos es {TRATAMIENTOS.get(cant[1][0])} con {cant[1][1]}\t')
main()    

# 4) Lucho adora las zanahorias. Podría pasar horas contándonos sobre las diferentes variedades de zanahorias, con sus
# diferentes sabores, colores, olores, texturas... 
# Nos ha contratado para que lo ayudemos a realizar la compra. Luego de investigar, ha reducido su interés a únicamente
# dos proveedores de zanahorias: Sus nombres comerciales son “ZANAHORÍN” y “ZANAHORÓN”.
# ZANAHORÍN y ZANAHORÓN son los proveedores de máxima calidad, y como la calidad de ambos es indistinguible
# (¡Incluso para un experto en zanahorias de la talla de Lucho!), lo importante es comprar al que tenga menor precio de
# los dos.
# Lucho quiere que lo ayudes con una función llamada zanahorias, que reciba los precios en pesos (por tonelada de
# zanahorias) de cada proveedor en UN string, y escriba el nombre del proveedor al cual conviene comprar. Si ambos
# venden a igual precio, se debe escribir el texto “DA IGUAL”.
# Datos de entrada:
# Se reciben en un único string con dos enteros entre 1 y 100000 inclusive, separados por un espacio:
# • El primero indica el precio al que vende “ZANAHORÍN”
# • El segundo el precio al que vende “ZANAHORÓN”.
# Datos de salida:
# Se debe escribir una única línea, con la palabra “ZANAHORÓN” o “ZANAHORÍN” (sin las comillas), según quién tenga
# mejor precio. Si ambos venden al mismo precio, se debe escribir en una única línea la frase “DA IGUAL” (sin las
# comillas). Nota: Toda la salida debe estar en letras mayúsculas, como se ha indicado.
# Ejemplo:
#  Si la entrada por parámetro fuera: 15223 17250
# La salida debería ser: ZANAHORÍN

def main()->None:
    pass
main()    

#-----------------------------------------Ejercicio 5----------------------------------------------------------
# 5) Números escalonados: Un número es escalonado, si sus dígitos están en orden estrictamente creciente.
# Por ejemplo, 359 es escalonado, 34 también, pero 5674 no es, y tampoco 5667.
# Se recibe un número entero por parámetro N > 10 (lo cual se debe validar).
# La salida debe decir si es un número escalonado o no lo es y a continuación indicar la cantidad de dígitos cuya secuencia
# fue escalonada.
# Datos de entrada:
# Se recibe un parámetro con el número entero N.
# Datos de salida:
# El programa debe imprimir por pantalla en una línea, conteniendo un único número: la cantidad de números
# escalonados que hay entre 10 y N, inclusive.
# Ejemplo1: Entrada: 359 - Salida: “Es escalonado”, 3
# Ejemplo2: Entrada: 24893471 - Salida: “No es escalonada”, 4
# def validar_numero()->int:
#     numero = input('ingrese un numero: ')
#     while not (int(numero)>10):
#         numero = input('Error!! Ingrese de nuevo el numero: ')
#     return numero    
# def escalonado(lista:list)->str:
#     contador = 0
#     for i in lista:
#         continuar = True
#         while continuar == True:
#             if lista[-2::1]:
#                 if lista[i]<lista[i+1]:
#                     contador += 1
#                 else:
#                     continuar = False   
#             if lista[0:-2:1]:
#                 if lista[i]<lista[i+1]:
#                     contador += 1            
            
# def main()->None:
#     lista = []
#     contador = 0
#     numero_str = validar_numero()
#     numero_list = [int(i) for i in numero_str]
        
# main()    