def crear_lista(cadena: str) -> list:
    lista = list()
    for letra in cadena:
        lista.append(letra)
    return lista
def obtener_pares(lista_numeros: list) -> list:
    """ Obtengo los numeros pares """
    pares = list()
    ya_guardados = list()
    for numero in lista_numeros:
        es_repetido = numero not in ya_guardados
        if lista_numeros.count(numero) > 1 and es_repetido:  # Si esta repetido y no fue guardado
            if int(numero) % 2 == 0:  # si es par
                pares.append(numero)
            else:  # Si es impar
                par_cercano = int(numero) - 1
                pares.append(str(par_cercano))
            ya_guardados.append(numero)
    return pares
def obtener_cadena_ordenada(cadena: str) -> str:
    lista_numeros = crear_lista(cadena)
    lista_numeros.sort()
    lista_pares = obtener_pares(lista_numeros)
    lista_pares.sort()
    return ','.join(lista_numeros + lista_pares)
def main() -> None:
    cadena_original = '275217'
    cadena_ordenada = obtener_cadena_ordenada(cadena_original)
    print("Original: ", cadena_original)
    print("Cadena ordenada: ", cadena_ordenada)
main()