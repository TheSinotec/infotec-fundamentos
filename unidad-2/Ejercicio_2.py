#Funcion de validación de cadena vacía y/o espacios vacíos
def no_vacio(cadena: str):
    #Se valida que la cadena esté vacía 
    if cadena == "":
        return False
    else:
        #Se valida que no sean espacios en blanco
        return False if set(cadena) == set(" ") else True
    
#Función de validación de numero entero
def es_numero(num: str):
    #Se valida cadena vacía
    if no_vacio(num):
        return False
    #Ciclo para verificar que el número no contenga caracteres no numericos
    for x in num:
        #Se agrega bandera de caracter numérico
        bandera = False
        #Validación de caracter digital
        if x in "1234567890":
            bandera = True
        else:
            return False
    #Se regresa True si la bandera se mantiene en True, False como excepción
    return bandera

#Función de validación de numero flotante
def es_flotante(num: str):
    #Se valida cadena vacía
    if no_vacio(num):
        return False
    #Se agrega bandera de validación de caracter numérico
    bandera = False
    #Se agrega contador de puntos decimales
    contador = 0
    #Ciclo de validación de digitos y contador de puntos decimales
    for x in num:
        #Se valida dígito y un unico punto decimal
        if x in "1234567890":
            bandera = True
        elif x == "." and contador < 1:
            #Se cuentan puntos
            contador += 1
        else:
            return False
    #Se valida la existencia de al menos un número
    if bandera:
        #Se regresa True si el numero flotante es menor o igual a 10, si no esta fuera de rango
        return True if (float(num) <= 10) else False
    else:
        return False

#Función de manejo de mensajes y captura de datos
def entrada_validada(mensaje: str, validacion, error: str):
    #Ciclo equivalente a do..while
    while True:
        #Se muestra un mensaje
        print(f"\n{mensaje}")
        #Se pide un valor por consola
        valor = input()
        #Si el valor cumple la validación se regresa el valor
        if validacion(valor):
            return valor
        else:
            #Mensaje de error
            print(f"\n\nATENCIÓN: {error} Intente de nuevo.")

#Sistema integrado (main)
def sistema_historial():
    #Se crea una lista vacía de datos
    data = []
    #Se generan entradas de datos validadas para la candidad de alumnos con sus mensajes de entrada y error, asi como funciones de evaluación
    alumnos = int(entrada_validada("Introduzca la cantidad de alumnos: ", es_numero, "Debe ser un número entero positivo."))
    #Se generan entradas de datos validadas para la candidad de materias con sus mensajes de entrada y error, asi como funciones de evaluación
    materias = int(entrada_validada("Introduzca la cantidad de materias: ", es_numero, "Debe ser un número entero positivo."))
    #Ciclo para generar registros segun la cantidad de alumnos
    for i in range(alumnos):
        #Se crea un diccionario de registro para cada alumno
        registro = {}
        #Se crea una lista para las materias
        tira = []
        #Se genera una entrada de datos validada para el nombre
        registro["nombre"] = entrada_validada(f"Nombre del alumno #{i + 1}: ", no_vacio, "No puede estar vacío el nombre")
        #Se genera una entrada de datos validada para la matricula
        registro["matricula"] = entrada_validada(f"Matricula del alumno {registro["nombre"]}: ", no_vacio, "No puede estar vacía su matrícula")
        #Ciclo para generar el registro de materias
        for j in range(materias):
            #Se agrega mediante entrada de datos validada la aprobación o no de la materia según una entrada flotante
            tira.append("Reprobada" if float(entrada_validada(f"Calificación de la materia #{j + 1} del alumno {registro["nombre"]}: ", es_flotante, "Debe ser un número positivo entre 0 y 10.")) <= 6.0 else "Aprobada")
        #Se agrega al registro la tira de materias
        registro["materias"] = tira
        #Se agrega el diccionario de registro a la lista de datos
        data.append(registro)
    #Se genera el historial académico de cada alumno según los registros de datos
    for x in data:
        #Se puestra mensaje personalizado de cada alumno
        print(f"\n\nEl alumno {x["nombre"]} de matricula {x["matricula"]} tiene el siguiente historial:")
        #Indice para mostrar
        indice = 1
        #Ciclo para generar la vista de todas las materias y su estatus de aprobación
        for y in x["materias"]:
            #Se muestra la materia y su aprovación
            print(f"Materia #{indice}: {y}")
            #Se incrementa el índice
            indice += 1

#Se inicializa el programa mediante la función principal
sistema_historial()
