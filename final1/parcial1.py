# 1) Informar el promedio de temperatura de cada sector.
# 2) Determinar el sector con mayor temperatura y el sector con menor temperatura.
# 3) Informar la hora de mayor y menor temperatura de cada sector.
# 4) Crear el archivo de seguridad respetando el formato requerido.
# 5) Informar cuantos tubos deben revisarse.
# 6) Informar el sector mas problemático (mayor numero de tubos a revisarse).
#   Norte(sector); 4(tubo); 09:14:22(hora); 382(temperatura) --> Ejemplo del archivo de temperatura.txt
import csv

def mostrar_promedio(sector:list)->float:
    contador = len(sector)
    temperatura_promedio = 0
    for temperatura in sector:
        temperatura_promedio += (int(temperatura[3]))
    temperatura_promedio = temperatura_promedio // contador
    return f'{temperatura_promedio}°C ({sector[0][0]})  '

def abrir_archivo()->list:
    archivos_datos = []
    with open ('temperatura.txt','r')as archivos:
        for archivo in archivos:
            archivo = archivo.rstrip().split(';')
            archivos_datos.append(archivo)
    return archivos_datos

def temperatura_minimo_maximo(archivos:list)->tuple:
    contador = 0
    maximo = 0
    minimo = 0
    for archivo in archivos:
        contador += 1
        if contador == 1:
            maximo = int(archivo[3])
            sector_maximo = archivo[0]
            minimo = int(archivo[3])
            sector_minimo = archivo[0]
        else:    
            if maximo < int(archivo[3]):
                maximo = int(archivo[3])
                sector_maximo = archivo[0]
            elif minimo > int(archivo[3]):
                minimo = int(archivo[3]) 
                sector_minimo = archivo[0]
        if contador == len(archivos):
            return [minimo,sector_minimo],[maximo,sector_maximo]

def hora_temperatura_minimo_maximo(sector)->tuple:
    maximo_temperatura = sorted(sector, key=lambda x:x[3],reverse=True)
    maximo_hora = maximo_temperatura[0][2]
    minimo_hora = maximo_temperatura[-1][2]
    return maximo_hora,minimo_hora

def archivo_seguridad(archivos)->None:
    archivo = sorted(archivos,key=lambda x:x[3],reverse=True)

    with open ('seguridad.csv','w',newline='',encoding='utf-8')as archivo_csv:
        csv_writer = csv.writer(archivo_csv,delimiter=',')
        csv_writer.writerow(["Temperatura","Sector+N° de tubo"])
        for i in archivo:
            temperatura = i[3]
            sector = i[0]
            numero_tubo = i[1]
            csv_writer.writerow((temperatura,f'{sector[0]}{numero_tubo}'))

def temperatura_seguridad()->list:
    tubos_a_revisar = []
    contador = 0
    with open ('seguridad.csv',encoding='utf-8')as seguridad_csv:
        csv_reader = csv.reader(seguridad_csv,delimiter=',')
        next(csv_reader)
        for row in seguridad_csv:
            row = row.rstrip('\n').split(',')
            if int(row[0])<385 or int(row[0])>395:
                contador += 1
                tubos_a_revisar.append(row)

    print(f'Se deben revisar {contador} tubos')
    return tubos_a_revisar            

def sector_problematico()->None:
    sector_problematicos = {
        'Oeste':0,'Sur':0,'Norte':0,'Este':0
        }
    sector_oeste = 0
    sector_este = 0
    sector_sur = 0
    sector_norte = 0
    sector_problematico = temperatura_seguridad()
    for tubo in sector_problematico: #[temperatura,sector+n de tubo] ->['382','O43']
        tubo_sector = tubo[1][0]
        if tubo_sector=='O':
            sector_oeste += 1
            sector_problematicos['Oeste'] = sector_oeste
        if tubo_sector=='N':
            sector_norte += 1
            sector_problematicos['Norte'] = sector_norte
        if tubo_sector=='S':
            sector_sur += 1
            sector_problematicos['Sur'] = sector_sur
        if tubo_sector=='E':
            sector_este += 1
            sector_problematicos['Este'] = sector_este
    sector_problematicos_ordenados = sorted(sector_problematicos.items(),key=lambda x:x[1],reverse=True)
    contador = 0
    sector_alto = []
    for i in sector_problematicos_ordenados:
        contador += 1
        if contador == 1:
            valor_mas_alto = i[1] 
        if contador == 1 or i[1] == valor_mas_alto:
            sector_alto.append(i[0])
    return sector_alto        

def main()->None:
    datos_archivos = abrir_archivo()
    norte = []
    sur = []
    oeste = []
    este = []
    for archivo in datos_archivos:
        if archivo[0] == 'Norte':
           norte.append(archivo) 
        if archivo[0] == 'Oeste':
           oeste.append(archivo) 
        if archivo[0] == 'Este':
           este.append(archivo) 
        if archivo[0] == 'Sur':
           sur.append(archivo) 
    print(f'La temperatura promedio de cada sector es {mostrar_promedio(norte)},{mostrar_promedio(oeste)},{mostrar_promedio(este)},{mostrar_promedio(sur)}\n')
    minimo_maximo = temperatura_minimo_maximo(datos_archivos)
    print(f'La temperatura mas baja pertenece al sector -> {minimo_maximo[0][1]} ',f'({minimo_maximo[0][0]} °C)','\n')
    print(f'La temperatura mas alta pertenece al sector -> {minimo_maximo[1][1]} ',f'({minimo_maximo[1][0]} °C)','\n')
    print(f'NORTE -> El registro de mayor temperatura: {hora_temperatura_minimo_maximo(norte)[0]} y de menor temperatura: {hora_temperatura_minimo_maximo(norte)[1]}')
    print(f'ESTE -> El registro de mayor temperatura: {hora_temperatura_minimo_maximo(este)[0]} y de menor temperatura: {hora_temperatura_minimo_maximo(este)[1]}')
    print(f'OESTE -> El registro de mayor temperatura: {hora_temperatura_minimo_maximo(oeste)[0]} y de menor temperatura: {hora_temperatura_minimo_maximo(oeste)[1]}')
    print(f'SUR -> El registro de mayor temperatura: {hora_temperatura_minimo_maximo(sur)[0]} y de menor temperatura: {hora_temperatura_minimo_maximo(sur)[1]}\n')
    archivo_seguridad(datos_archivos)
    print(f'El sector o los sectores mas comprometidos son: {sector_problematico()}')

main()

