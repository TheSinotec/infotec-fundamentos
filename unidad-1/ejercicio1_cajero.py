# Variables para contar billetes
billetes_1000 = 10
billetes_500 = 10
billetes_200 = 10
billetes_100 = 10
billetes_50 = 10
# Variables para billetes a entregar
entregar_1000 = 0
entregar_500 = 0
entregar_200 = 0
entregar_100 = 0
entregar_50 = 0
monto_restante = 0
# Agrego control para el monto
monto = -1
while monto != 0:
    # Monto máximo
    maximo = billetes_1000*1000 + billetes_500*500 + billetes_200*200 + billetes_100*100 + billetes_50*50
    # Muestra de inventario
    print(f"\n\nMONTO MAXIMO DISPONIBLE: ${str(maximo)}")
    # Iniciamos el sistema
    print("\n--- Dispensadora de Billetes ---")
    # Solicitar monto
    print("\nIngrese el monto a retirar (0 para salir): ")
    entrada = input()
    flag = False
    # Validación de entero
    for x in entrada:
        # Bandera de caracter
        flag = False
        # String con todos los dígitos
        for y in "1234567890":
            # Si x esta es un dígito se marca
            if x == y:
                flag = True
                break
        # La bandera debe ser True SIEMPRE
        if not flag:
            break
    # Lógica de cajero
    if flag:
        # Transformamos el valor dato a un tipo de dato entero
        monto = int(entrada)
        if (monto > maximo or bool(monto % 50)) and maximo != 0:
            # No se expende dinero (Monto demasiado grande)
            print(f"\nNo se puede cumplir la orden (Se excede el monto máximo).\nSe requisitó: ${entrada}\nSe expende: $0")
        elif monto == 0:
            # Escape
            print("\nOperación cancelada.\nSe expende: $0")
        elif maximo == 0:
            # No se expende dinero (No hay dinero)
            print(f"\nEl cajero no tiene dinero.\nSe requisitó: ${entrada}\nSe expende: $0")
        else:
            # Se genera una copia del monto para sustraer
            monto_restante = monto
            # Se compara residuo y existencia de los billetes de 1000
            if monto_restante // 1000 > billetes_1000:
                entregar_1000 = billetes_1000
            else:
                entregar_1000 = monto_restante // 1000
            # Se sustrae la mayor cantidad de billetes de 1000
            monto_restante -= entregar_1000 * 1000
            # Se compara residuo y existencia de los billetes de 500
            if monto_restante // 500 > billetes_500:
                entregar_500 = billetes_500
            else:
                entregar_500 = monto // 500
            # Se sustrae la mayor cantidad de billetes de 500
            monto_restante -= entregar_500 * 500
            # Se compara residuo y existencia de los billetes de 200
            if monto_restante // 200 > billetes_200:
                entregar_200 = billetes_200
            else:
                entregar_200 = monto_restante // 200
            # Se sustrae la mayor cantidad de billetes de 200
            monto_restante -= entregar_200 * 200
            # Se compara residuo y existencia de los billetes de 100
            if monto_restante // 100 > billetes_100:
                entregar_100 = billetes_100
            else:
                entregar_100 = monto_restante // 100
            # Se sustrae la mayor cantidad de billetes de 100
            monto_restante -= entregar_100 * 100
            # Se compara residuo y existencia de los billetes de 50
            if monto_restante // 50 > billetes_50:
                entregar_50 = billetes_50
            else:
                entregar_50 = monto_restante // 50
            # Se sustrae la mayor cantidad de billetes de 50
            monto_restante -= entregar_50 * 50
            # Si el resto no es completo, no hay billetes para completar la operación
            if monto_restante != 0:
                # No se expende dinero (No hay billetes para completar).
                print(f"\nNo se puede cumplir la orden.\nSe requisitó: ${entrada}\nSe expende: $0")
            else:
                # Se toman los billetes para surtir la orden
                billetes_1000 -= entregar_1000
                billetes_500 -= entregar_500
                billetes_200 -= entregar_200
                billetes_100 -= entregar_100
                billetes_50 -= entregar_50
                # Se entregan en pantalla y se añade un resumen de la operación
                print("\nSe requisitó: $", entrada,
                      "\nSe expende: $", entregar_1000 * 1000 + entregar_500 * 500 + entregar_200 * 200 + entregar_100 * 100 + entregar_50 * 50,
                      "\nBilletes:",
                      bool(entregar_1000)*("\n$1000: " + str(entregar_1000)),
                      bool(entregar_500)*("\n$500: " + str(entregar_500)),
                      bool(entregar_200)*("\n$200: " + str(entregar_200)),
                      bool(entregar_100)*("\n$100: " + str(entregar_100)),
                      bool(entregar_50)*("\n$50: " + str(entregar_50)))

    else:
        # No se expende dinero (Monto incorrecto)
        print(f"\nMonto incorrecto.\nSe requisitó: ${entrada}\nSe expende: $0")

