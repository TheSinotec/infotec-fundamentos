#pip install {pandas, openpyxl}

import pandas as pd

# 1. Carga los archivos
df_estudiantes = pd.read_csv("./archivos/respuestas_estudiantes.csv")
df_correctas = pd.read_excel("./archivos/respuestas_correctas.xlsx")

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

# 7. Guarda resultados
df_estudiantes.to_csv("resultados_examen.csv", index = False)
print("\nResultados guardadps en 'resultados_examen.csv")
