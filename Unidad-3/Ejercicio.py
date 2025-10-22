#pip install {pandas, openpyxl}

import pandas as pd

def extraer_extension(ruta: str):
    partes = ruta.split(".")
    return partes[2] if (len(partes) == 3 and partes[2] in ["xlsx", "xml", "csv"]) else False

def manejar_archivo(ruta: str, metodo, export: bool = False):
    extension = extraer_extension(ruta)
    return False if not bool(extension) else (
        metodo(ruta) if not export else (
            metodo(ruta, index = False, parser = "etree") if extension == "xml" else metodo(ruta, index = False)
        )
    )

def calificar_examenes(df_correctas, df_estudiantes):
    # 2. Obtener loas preguntas usando métodos
    preguntas = df_correctas["Pregunta"].values

    # 3. Crear diccionario de respuestas correctas
    clave_respuestas = {} # Paso 1: Creamos un diccionario vacío
    for i in range(df_correctas.shape[0]): # Paso 2: Recorremos cada fila
        # Paso 3: Extraemos pregunta y respuesta
        pregunta = df_correctas["Pregunta"].iloc[i]
        respuesta = df_correctas["Respuesta"].iloc[i]
        # Paso 4: Almacenamos en el diccionario
        clave_respuestas[pregunta] = respuesta

    # 4. Calcular puntuación de cada estudiamte
    df_estudiantes["Puntuación"] = 0 # Inicializa la columna de puntuación
    for p in preguntas: # Recorre cada pregunta
        respuesta_correcta = clave_respuestas[p] # Obtiene la respuesta correcta
        # Compara respuestas y suma 1 punto por cada acierto:
        df_estudiantes["Puntuación"] = df_estudiantes["Puntuación"].add(
            (df_estudiantes[p] == respuesta_correcta).astype(int)
        )

    # 5. Mostrar detalle completo de respuestas
    df_detalle = df_estudiantes.copy() # Copia el DataFrame original

    for p in preguntas:
        # Marca errores añadiendo X donde no coinciden:
        df_detalle[p] = df_detalle[p].where(
            df_detalle[p] == clave_respuestas[p],
            df_detalle[p] + "X"
        )

    # Ordena por puntuación (mayor a menor):
    df_detalle = df_detalle.sort_values("Puntuación", ascending = False)
    print("Leyenda: Respuesta X = Incorrecta")
    print(df_detalle.to_string(index = False)) # Muestra sin índices

    # 6. Mostrar resultados resumidos
    print("\n=== RESULTADOS DE LOS ESTUDIANTES ===")
    print(df_estudiantes[["Nombre", "Puntuación"]].sort_values("Puntuación", ascending = False).to_string(index = False))



# 1. Carga los archivos
#df_estudiantes = pd.read_csv("./respuestas_estudiantes.csv")
#df_correctas = pd.read_excel("./respuestas_correctas.xlsx")
#df_correctas.to_xml("./correctas.xml", index=False, parser="etree")
#df_correctas = manejar_archivo("./respuestas_correctas.xlsx", pd.read_excel)
#print(df_correctas)
#print(manejar_archivo("./respuesta22.xlsx", df_correctas.to_excel, True))


print("\nPara comenzar ingrese la ruta del archivo que desea usar para la evaluación (el nombre del archivo debe contener la extención):\n")
#IMPUT
entrada = "./respuestas_correctas.xlsx"
match(extraer_extension(entrada)):
    case "xlsx":
        df_correctas = manejar_archivo(entrada, pd.read_excel)
    case "xml":
        df_correctas = manejar_archivo(entrada, pd.read_xml)
    case "csv":
        df_correctas = manejar_archivo(entrada, pd.read_csv)
    case default:
        print("\nFormato de ruta incompleto (la ruta debe comenzar con la raíz './' seguido de las carpetas que contienen el archivo asi"\
              " como el nombre del archivo '.' extensión). \nSe admiten archivos csv, xlsx y xml. Intentelo nuevamente.\n\n")
        
#CALIFICA
#OUTPUT
while (entrada not in ["xlsx", "csv", "xml", "n"]):
    print("\n¿Desea exportar los datos? Teclee: \n[XLSX]: Exportar en formato xlsx\n[CSV]: Exportar en formato csv\n"\
          "[XML]: Exportar en formato xml\n [N]: Salir sin exportar\n\n")
    entrada = "csv"
if entrada != "n":
    while ("\\" in entrada or "." in entrada):
        print("\nIngrese el nombre de su archivo")
        entrada = "./respuestas_correctas.xlsx"
match(entrada):
    case "xlsx":
        manejar_archivo(entrada, df_correctas.to_excel, True)
    case "xml":
        manejar_archivo(entrada, df_correctas.to_xml, True)
    case "csv":
        manejar_archivo(entrada, df_correctas.to_csv, True)
    case "no":
        print("No se ha guardado ningún archivo")
    case default:
        print(f"\n[{entrada}] NO se considera como un formato válido. \nSe admiten archivos csv, xlsx y xml. Intentelo nuevamente.\n\n")
