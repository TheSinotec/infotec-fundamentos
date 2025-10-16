#Función de validación de carácter numérico
def es_numero(num: str):
    #Se regresa True si el caracter es numérico, False si no
    return True if num in "0123456789" else False

#Funcion de validación de fecha realista
def fecha_real(dia: int, mes: int, anio: int):
    #Se genera un diccionario de días máximos válidos
    meses = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 31, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    #Se invalida la fecha cada que los días no coincidan con sus meses o el año sea anterior a 1901 o mayor a 2025 [No se validad biciestos]
    return False if (dia > meses[mes] or anio < 1901 or anio > 2025) else True

#Función de validación de formato de entrada 
def validar_entrada(entrada: str):
    #Si la entrada inicia o termina en guión se regresa False
    if entrada == "" or entrada[0] == "-" or entrada[-1] == "-":
        return False
    #Se define una lista para separar las partes del string
    partes = []
    #Se define un índice para recorrer el arreglo
    indice = -1
    #Se define un indice detector de posiciones "-"
    ultimo_indice = 0
    #Se define un contador de segmentos
    contador = 0
    #Ciclo para separar el arreglo
    for x in entrada:
        #Avanzamos en el arreglo
        indice += 1
        #Si el caracter mo es un número o un separador o la cantidad de segmentos entre separadores es mayor a 3, se regresa False
        if ((not es_numero(x)) and (x != "-")) or (contador >= 4):
            return False
        #Si el caracter es un separador se genera un segmento
        elif x == "-":
            #Se cuenta el segmento
            contador += 1
            #Si el segmento desde el último separador no es el final, se agrega el par [segmento a la lista, cantidad de caracteres] a la lista, si no se regresa False
            if entrada[ultimo_indice: indice] != "":
                partes.append([entrada[ultimo_indice: indice], indice - ultimo_indice])
            else:
                return False
            #Se reasigna el índice del ultimo separador
            ultimo_indice = indice + 1
    #Se cuenta el segmento final que no tiene separador al final
    contador += 1
    #Se agrega el par [segmento a la lista, cantidad de caracteres] que queda residual al final de la cadena
    partes.append([entrada[ultimo_indice:], indice + 1 - ultimo_indice])
    #Se valida si se excede la cantidad de tres segmentos, se manda False si se excede
    if (contador != 3):
        return False
    else:
        #Se valida que la dimensión de cada segmento sea adecuada al formato, si no también se manda False
        if (partes[0][1] != 2) or (partes[1][1] != 2) or (partes[2][1] != 4):
            return False
        else:
            #Se regresa una lista con la fecha en número [d,m,a] si la fecha es real para cada mes, en caso contrario se manda False
            return [int(partes[0][0]), int(partes[1][0]), int(partes[2][0])] if fecha_real(int(partes[0][0]), int(partes[1][0]), int(partes[2][0])) else False

#Función para validar que la fecha no supere la fecha actual
def compara_fechas(fecha: list, dia_hoy: int):
    #Regresa Falso si el mes o el día y mes no son compatibles (fecha que supera "hoy"), si es correcta se regresa True
    return False if fecha[1] > 10 or (dia_hoy < fecha[0] and 10 == fecha[1]) else True

#Función para calcular la edad según la fecha y si cumple años
def calcular_edad(fecha: list, dia_hoy: int):
    #Si el mes y día coinciden, se marca una bandera de cumpleaños
    if (fecha[1] == 10) and (fecha[0] == dia_hoy):
        cumple = True
    else:
        cumple = False
    #Se muestra mensaje de edad con la edad y si cumple años (o si nació hoy)
    return "\nSu edad es: " + str(2025 - fecha[2]) + cumple*" ¡Feliz cumpleaños!" + (not bool(2025 - fecha[2]))*" NACISTE HOY Xd"

#Función principal del sistema
def sistema_fecha(dia: int):
    #Se define una entrada vacía
    entrada = ""
    #Se define una lista para la fecha vacía
    fecha = []
    #Si la fecha es vacía o False el ciclo se mantiene pidiendo la fecha de nacimiento
    while not bool(fecha):
        #Mensaje de bienvenida
        print(f"\nIngrese la fecha de nacimiento, el formato de fecha debe ser DD-MM-AAAA, contemplando que sólo se aceptan fechas entre 1901 y 2025:")
        #Entrada de datos
        entrada = input()
        #Obtención de fecha validada y segmentada
        fecha = validar_entrada(entrada)
        #Si la fecha fue obtenida adecuadamente se calcula la edad, si no se manda mensaje y se repite el ciclo
        if bool(fecha):
            #Si las fechas son válidas se calcula la edad
            if compara_fechas(fecha, dia):
                #Se valida y muestra la edad
                print(calcular_edad(fecha, dia))
            else:
                #Se manda mensaje de atención para fechas futuras al día
                print(f"\n\nATENCIÓN: La fecha ingresada es mayor al {dia}-10-2025 (fecha actual). Ingrese una fecha válida.")
                #Se vacía la fecha
                fecha = []
        else: 
            print("\n\nATENCIÓN: La fecha ingresada no cumple con los requisitos de formato y año. Ingrese una fecha válida.")



#Día asociado a OCTUBRE 2025 // FECHA ESTATICA
dia = 17
#Se inicializa el programa mediante la función principal
sistema_fecha(dia)
