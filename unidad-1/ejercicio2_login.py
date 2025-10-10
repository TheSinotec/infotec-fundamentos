# Credenciales válidas (como variables individuales)
usuario_correcto = "admin"
clave_correcta = "1234"
# Se define la cantidad de intentos
intentos = 3
# Bucle de intentos
while intentos != 0:
    # Mensaje de carga
    print("\n--- Sistema de Inicio de Sesión ---")
    print(f"Intentos restantes: {intentos}")
    # Solicitar credenciales
    usuario = input("Usuario: \n")
    clave = input("Contraseña: \n")
    # Validación de casos
    if ((usuario == usuario_correcto) and (clave == clave_correcta)):
        # Logeo exitoso
        print(f"\nBienvenido {usuario}")
        # Salida del sistema
        intentos = 0
    else:
        # Errores asociado a campo faltante y no coincidencia
        print((not bool(usuario) or not bool(clave)) * "Error de autenticación. Campo faltante.\n" +
                                                       "El usuario o la contraseña no coinciden.")
        # Se consume un intento
        intentos -= 1
        # Mensaje de bloqueo
        if intentos == 0:
            print("\nSe ha bloqueado el sistema por exceder la cantidad de intentos. Intente más tarde.")
