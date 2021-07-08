# 4) Crear una función que reciba un string que contiene números y los ordene de menor a mayor; pero teniendo las siguientes consideraciones: Si hay números repetidos (solo van a poder estar repetidos 1 vez): 
# oLos números repetidos pares irán copiados en otra lista. (Además de estar en la ordenada) 
# oLos números repetidos impares deberán ir en la misma lista que los anteriores (además de estar en la ordenada), pero escritos como el número menor y par más próximo que tengan.  
# Ejemplo: Si es 5, su par menor más cercano es 4. 
# La función debe devolver un string con los números ordenados, separados por comas y además los repetidos ordenados al final. Ejemplo: cadena = '275217' >>>1, 2, 2, 5, 7, 7, 2, 6

def numero_str(numero:str)->str:
    lista_repetidos = []
    numero = [int(i) for i in numero] #numero ahora es una lista
    numero = sorted(numero)
    for i in numero: 
        if numero.count(i)>2:
            numero.remove(i)
        if numero.count(i)>1:
            lista_repetidos.append(i)
    for repetidos in lista_repetidos:
        if lista_repetidos.count(repetidos)>1:
            lista_repetidos.remove(repetidos)
        if repetidos%2!=0:
            repetidos -= 1
    numero.extend(lista_repetidos)                     
    numero =  [str(i) for i in numero]
    return numero


def main()->None:
    num_str = input('Ingrese un numero: ')

    print(numero_str(num_str))

main()