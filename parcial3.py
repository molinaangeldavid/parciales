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
#  c) Emita un reporte que informe el monto total de tratamientos vendidos.
#  d) Emita un reporte que informe el total de pacientes nuevos y viejos.
#  e) Emita un reporte que informe cuál es el tratamiento más solicitado por los pacientes nuevos.
# A tener en cuenta: Se considera que un paciente es *nuevo* en caso de que el mismo haya asistido únicamente a 1
# consulta con el profesional.

TRATAMIENTOS = {
    1: ['Higiene Profunda',1500],
    2: ['Tratamiento Acné',1500],
    3: ['Tratamiento tensor con aparatologia',1800],
    4: ['Tratamiento revitalizante',3000]
}

def alta_cliente(paciente)->None:
    print('El cliente con el dni ingresado no se encuentra en la base de datos. Registrarlo\n')
    n_dni = ingreso_usuario
    n_nombre_apellido = input('Ingrese nombre y apellido del paciente: ')

def ingreso_usuario()->None:
    dni = input('Ingrese el DNI del paciente: ')
    while not (dni.isnumeric() and  int(dni)>10000000 and int(dni)<88888888):
        dni = input('Error!!Ingreso invalido. Vuelva a intentarlo: ')
    dni = int(dni)
    return dni    

def main()->None:
    paciente = {}
    init = False
    while not init:
        db_dni = [i for i in paciente.keys()]
        dni = ingreso_usuario(paciente)
        if dni not in db_dni:
            alta_cliente()    
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
def validar_numero()->int:
    numero = input('ingrese un numero: ')
    while not (int(numero)>10):
        numero = input('Error!! Ingrese de nuevo el numero: ')
    return numero    
def escalonado(lista:list)->str:
    contador = 0
    for i in lista:
        continuar = True
        while continuar == True:
            if lista[-2::1]:
                if lista[i]<lista[i+1]:
                    contador += 1
                else:
                    continuar = False   
            if lista[0:-2:1]:
                if lista[i]<lista[i+1]:
                    contador += 1            
            
def main()->None:
    lista = []
    contador = 0
    numero_str = validar_numero()
    numero_list = [int(i) for i in numero_str]
        
main()    