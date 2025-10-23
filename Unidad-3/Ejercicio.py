#pip install {pandas, openpyxl}

import pandas as pd

def extraer_extension(ruta: str):
    """
    Funcion que toma una ruta en forma de cadena de texto y extrae la extension del archivo. Solo se permiten ["xlsx", "xml", "csv"] como extension.

    Parameters:
        ruta (String): Representa una ruta de un archivo de formato ["./<ruta>/<archivo>.<extension>].
    
    Returns:
        (String): La extension del archivo contenido en la ruta [<extension>].
        (Boolean == False): Si no cumple la validacion de la ruta
    
    Exceptions:
        (FileNotFoundError): Archivo no existe.
    """
    #Se segmenta la entrada segun puntos
    partes = ruta.split(".")
    #Se regresa la extension si la ruta tiene el formato de ruta y si es uno de los formatos permitidos, False si no
    return partes[2] if (len(partes) == 3 and partes[2] in ["xlsx", "xml", "csv"]) else False

def manejar_archivo(ruta: str, metodo, export: bool = False):
    """
    Funcion que recibe una ruta de archivo, un metodo y una bandera. Aplica el método si la extensión 

    Parameters:
        ruta (String): Representa una ruta de un archivo de formato ["./<ruta>/<archivo>.<extension>].
    
    Returns:
        (String): La extension del archivo contenido en la ruta [<extension>].
        (Boolean == False): Si no cumple la validacion de la ruta
    
    Exceptions:
        (FileNotFoundError): Archivo no existe.
    """
    #Se extre la extension de la ruta
    extension = extraer_extension(ruta)
    #Se entrega falso si la extension no es valida o la ruta
    return False if not bool(extension) else (
        #Si la exportacion no esta activa se ejecuta el metodo sobre la ruta
        metodo(ruta) if not export else (
            #Si está activo el modo de exportacion se valida si es xml y se pasan parametros de libreria
            metodo(ruta, index = False, parser = "etree") if extension == "xml" else metodo(ruta, index = False)
        )
    )

def calificar_examenes(df_correctas, df_estudiantes):
    #Obtenemos las preguntas usando metodos
    preguntas = df_correctas["Pregunta"].values
    #Inicializamos diccionario de respuestas correctas
    clave_respuestas = {}
    #Ciclo para recorrer las columnas
    for i in range(df_correctas.shape[0]):
        #Se extrae pregunta y respuesta
        pregunta = df_correctas["Pregunta"].iloc[i]
        respuesta = df_correctas["Respuesta"].iloc[i]
        #Almacenamos en el diccionario
        clave_respuestas[pregunta] = respuesta
    #Se inicializa la columna de puntuacion
    df_estudiantes["Puntuación"] = 0 
    #Se calcula la puntuacion de cada estudiante
    for p in preguntas:
        #Se obtiene la respuesta correcta
        respuesta_correcta = clave_respuestas[p] 
        #Se comparan respuestas y suma 1 punto por cada acierto
        df_estudiantes["Puntuación"] = df_estudiantes["Puntuación"].add(
            (df_estudiantes[p] == respuesta_correcta).astype(int)
        )
    #Se copia el DataFrame original
    df_detalle = df_estudiantes.copy()
    #Se vuelve a recorrer para marcar errores
    for p in preguntas:
        #Se marcan errores añadiendo X donde no coinciden:
        df_detalle[p] = df_detalle[p].where(
            df_detalle[p] == clave_respuestas[p],
            df_detalle[p] + "X"
        )
    #Se ordena por puntuación (mayor a menor):
    df_detalle = df_detalle.sort_values("Puntuación", ascending = False)
    print("Leyenda: Respuesta X = Incorrecta")
    print(df_detalle.to_string(index = False))
    #Se muestran resultados resumidos
    print("\n=== RESULTADOS DE LOS ESTUDIANTES ===")
    print(df_estudiantes[["Nombre", "Puntuación"]].sort_values("Puntuación", ascending = False).to_string(index = False))
    return df_estudiantes

def casos(mensaje_entrada: str, metodo, export: bool = False):
    #Se inicializa entrada vacía
    entrada = ""
    #Bucle para mantener ciclado el proceso hasta que la extensión de la ruta sea válida
    while(not extraer_extension(entrada)):
        #Se muestra un mensaje y se genera una entrada de datos por consola
        entrada = input(f"\n{mensaje_entrada}\n")
        #Se generan casos según la extensión del archivo
        match(extraer_extension(entrada)):
            case "xlsx":
                #Caso para formato EXCEL
                return manejar_archivo(entrada, (metodo.read_excel if not export else metodo.to_excel), export)
            case "xml":
                #Caso para formato XML
                return manejar_archivo(entrada, (metodo.read_xml if not export else metodo.to_xml), export)
            case "csv":
                #Caso para formato CSV
                return manejar_archivo(entrada, (metodo.read_csv if not export else metodo.to_csv), export)
            case default:
                #Se muestra un mensaje de error y se reinicia la entrada
                print("\nFormato de ruta incompleto (la ruta debe comenzar con la raíz './' seguido de las carpetas que contienen el archivo asi"\
                      " como el nombre del archivo '.' extensión). \nSe admiten archivos csv, xlsx y xml. Intentelo nuevamente.\n\n")
                entrada = ""

def inicio():
    #Se pide el archivo de preguntas y respuestas correctas
    df_correctas = casos("Para comenzar ingrese la ruta del archivo que desea usar para la evaluación (el nombre del archivo debe contener la extención):", pd, False)
    #Se pude el archivo de respuestas de los alumnos
    df_estudiantes = casos("Ingrese la ruta del archivo que desea usar para evaluar (el nombre del archivo debe contener la extención):", pd, False)
    #Se califica y muestran resultados
    resultado = calificar_examenes(df_correctas, df_estudiantes)
    #Se inicializa una entrada vacia
    entrada = ""
    #Bucle para preguntar si se desea exportar o no archivo
    while (entrada not in ["s", "S", "n", "N"]):
        #Se muestra mensaje y se pide respuesta por teclado
        entrada = input("\n¿Desea exportar los datos? Teclee: \n[S]: Para exportar archivo \n[N]: Para salir sin exportar\n\n")
    #Se valida si la respuesta es afirmativa
    if entrada in "sS":
        #Se pide la ruta de exportacion, si se completa se manda mensaje de salida
        if casos("Ingrese la ruta con el archivo que desea exportar (el nombre del archivo debe contener la extención):", resultado, True) == None:
            #Se muestra mensaje de operacion finalziada
            print("\nSe exportó el archivo exitosamente")
        else:
            #Se muestra mensaje de export fallido
            print("\nOcurrio un error, vuelva a intentarlo")
    else: 
        #Respuesta negativa
        print("\nNo se exportó ningún archivo")

#Se ejecuta el algoritmo principal (main)
inicio()
