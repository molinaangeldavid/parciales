#--------------------------Ejercicio 1----------------------------------------------
# 1) a)Pase a base 10 el siguiente número expresado en base 6:
# 32442,51
# 4490,861111 base 10
#--------------------------Ejercicio 2----------------------------------------------
# b)Pasar el siguiente número en base 10 a base 9 con error menor o igual a 10-4:
# 6658,633
# 10117,56241 base 9
#--------------------------Ejercicio 3----------------------------------------------
# c) Pasar el siguiente número de base 4 a base 16 y justifique el método por el cual
# decidió hacer la conversión:
# 1223,23
# 5B,B base 16
#--------------------------Ejercicio 4----------------------------------------------
# 2) Escriba una función que dada una lista de denominaciones de billetes de la moneda
# corriente de un país, permita descomponer un importe otorgado por el usuario en las
# cantidades correspondientes a cada una de las denominaciones cual si fuera un cajero
# automático y suponiendo que siempre elige otorgar billetes del mayor valor posible. La
# función debe controlar que el importe sea factible de ser descompuesto y devolver un
# diccionario con la descomposición.
# Construya el programa principal donde utiliza dicha función.
# Ej:
# Lista = [10,20,50,100,200,500,1000]
# Valor = 1690
# Diccionario = {10:0,20:2,50:1;100:1;200:0;500:1;1000:1}

# def convertir(diccionario:dict,lista_billetes:list)->dict:
#     lista_billetes =[]
#     denominacion = input('Ingresar las denominaciones separadas por coma: ')
#     billete = denominacion.split(',')

#     for valor in billete:
#         valor = int(valor)
#         lista_billetes.append(valor)
#     lista_billetes.sort(reverse=True)
#     dinero = int(input('Ingrese cantidad de dinero que desea descomponer: '))
    
#     for denominaciones in lista_billetes:
#         if denominaciones<dinero:
#             resto = dinero // denominaciones
#             diccionario[denominaciones] = resto
#             dinero -= denominaciones*resto
#         if dinero == 1:
#             diccionario[1] = 1
#     return diccionario        

# def main()->None:
#     diccionario = {}
#     lista_billetes =[]
#     print(convertir(diccionario,lista_billetes))
# main()    
# --------------------------Ejercicio 5------------------------------------------------
# 3) Para celebrar el Día del Niño, en una plaza de gran extensión, se ha construido un
# caminito de baldosas cuadradas de hormigón de 3 colores: blanco, gris y negro. El
# caminito no tiene bifurcaciones y para que quedase más vistoso, se cuidó que las
# baldosas contiguas tuvieran diferente color.
# Lamentablemente el caminito ha perdido muchas de sus baldosas, ya que debieron ser
# quitadas para realizar un complejo tendido de cañerías. La figura muestra el estado
# actual del caminito.
# Los huecos dejados por las baldosas removidas se muestran cuadriculados. Quienes
# deben reconstruir el caminito desean dejarlo tal como estaba, pero no se llevó el 
# registro de los colores y ubicaciones de las baldosas removidas. Por lo tanto, se decide
# reconstruirlo respetando las que quedaron siguiendo la consigna original de que las
# contiguas no queden del mismo color, comprando las baldosas nuevas que hagan falta.
# Para ayudar en la reconstrucción se pide que escriba una función caminito(BALDOSAS)
# que devuelva un posible diseño para reconstruir el caminito y que también lo escriba
# por pantalla.
# Su parámetro es “baldosas”: una PALABRA conteniendo caracteres ‘B’ (blanco), ‘N’
# (negro), ‘G’ (gris) o ‘R’ (removido) separadas con coma “,” describiendo la vereda en su
# estado actual, esperando que sustituyas las ‘R’ por las letras que describan los colores
# de tu propuesta. La longitud de la palabra no es conocida.
# Tu propuesta de caminito deberá ser devuelta por la función y escrita por pantalla la
# palabra con la propuesta.
# Ejemplo:
# El parámetro BALDOSAS describe la figura y contiene: R,G,N,R,R,N,R,R,R,B,R,N
# El programa deberá escribir por pantalla una línea como la siguiente BGNBGNGBGBGN

#colores blanco 'B', gris 'G', negro 'N' y removido 'R'
import random

def in_str()->list:
    string = input('Ingresa separadas por coma el estado del caminito: ')
    baldosas = string.upper()
    baldosas = baldosas.split(',')
    return baldosas

def caminito(baldosas)->None: 
    '''
    PRE: Ingresa una cadena de texto separadas por comas, la cual representan el estado actual de las baldolas 
    POST: Retorna otra cadena de texto que indica como quedarian las baldosas con su estado final
    '''
    # Ejemplo pre R,G,N,R,R,N,R,R,R,B,R,N
    # Ejemplo post BGNBGNGBGBGN
    for baldosa in baldosas:
        if baldosa == 'R':
            baldosa = random.choice('G','B','N')
        if baldosa == baldosas[0] and baldosa == 'R' or baldosa == baldosas[1]:
            baldosa = 'G'
        if baldosa is baldosas[1] and baldosa == 'R': 
            baldosa = 'B'    
        if baldosa is baldosas[-1] and baldosa == 'R':
            pass
    resultado = ''.join(baldosas)
    return resultado

def main()->None:
    init = False
    while not init:
        print('Estado: N(negro),B(blanco),G(gris),R(removido)')
        baldosas = in_str()
        if 'N' in baldosas and 'G' in baldosas and 'R' in baldosas and 'B' in baldosas:
            print(caminito(baldosas))
            init = True
        else:
            init = False

main()    