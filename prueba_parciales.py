diccionario = {'1':5,'3':5,'5':8}
suma = diccionario.get('3')
suma += 10
diccionario['3'] = suma
print(diccionario)
