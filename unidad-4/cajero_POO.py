class Cajero:
    """
    Representa el cajero automatico

    Attributes:
        billetes_1000 (Integer): [Cantidad de billetes de $1000] Por defecto 10.
        billetes_500 (Integer): [Cantidad de billetes de $500] Por defecto 10.
        billetes_200 (Integer): [Cantidad de billetes de $200] Por defecto 10.
        billetes_100 (Integer): [Cantidad de billetes de $100] Por defecto 10.
        billetes_50 (Integer): [Cantidad de billetes de $50] Por defecto 10.
    
    Methods:
        monto_maximo(None): Obtiene la cantidad maxima entregable.
        retirar(monto: int = None): Realiza el retiro y actualiza el inventario.
    """
    
    #Se inicializan las variables en el constructor
    def __init__(self, billetes_1000 = 10, billetes_500 = 10, billetes_200 = 10, billetes_100 = 10, billetes_50 = 10):
        """
        Parameters:
            billetes_1000 (Integer): [Cantidad de billetes de $1000] Por defecto 10.
            billetes_500 (Integer): [Cantidad de billetes de $500] Por defecto 10.
            billetes_200 (Integer): [Cantidad de billetes de $200] Por defecto 10.
            billetes_100 (Integer): [Cantidad de billetes de $100] Por defecto 10.
            billetes_50 (Integer): [Cantidad de billetes de $50] Por defecto 10.
        """
        self.__billetes_1000 = billetes_1000
        self.__billetes_500 = billetes_500
        self.__billetes_200 = billetes_200
        self.__billetes_100 = billetes_100
        self.__billetes_50 = billetes_50
    
    #Metodo privado para la obtencion del monto maximo
    def __monto_maximo(self):
        """
        Metodo que calcula el monto maximo disponible en el cajero

        Parameters:
            (None): No recibe nada
        
        Returns:
            (Integer): El monto maximo disponible
        """
        #Calcula y regresa el monto maximo
        return self.__billetes_1000*1000 + self.__billetes_500*500 + self.__billetes_200*200 + self.__billetes_100*100 + self.__billetes_50*50

    #Metodo publico para retiro de efectivo del cajero
    def retirar(self, monto: int):
        """
        Metodo que ejecuta el retiro de efectivo del cajero.

        Parameters:
            monto (Integer): El monto requisitado por el usuario.
        
        Returns:
            (None): No retorna nada.
        """
        #Se obtiene el monto maximo
        maximo = self.__monto_maximo()
        if (monto > maximo or bool(monto % 50)) and maximo != 0:
            # No se expende dinero (Monto demasiado grande)
            print(f"\nNo se puede cumplir la orden (No hay billetes para completar su petición).\nSe requisitó: ${monto}\nSe expende: $0")
        elif monto == 0:
            # Escape
            print("\nOperación cancelada.\nSe expende: $0")
        elif maximo == 0:
            # No se expende dinero (No hay dinero)
            print(f"\nEl cajero no tiene dinero.\nSe requisitó: ${monto}\nSe expende: $0")
        else:
            entregar_1000 = 0
            entregar_500 = 0
            entregar_200 = 0
            entregar_100 = 0
            entregar_50 = 0
            # Se genera una copia del monto para sustraer
            monto_restante = monto
            # Se compara residuo y existencia de los billetes de 1000
            if monto_restante // 1000 > self.__billetes_1000:
                entregar_1000 = self.__billetes_1000
            else:
                entregar_1000 = monto_restante // 1000
            # Se sustrae la mayor cantidad de billetes de 1000
            monto_restante -= entregar_1000 * 1000
            # Se compara residuo y existencia de los billetes de 500
            if monto_restante // 500 > self.__billetes_500:
                entregar_500 = self.__billetes_500
            else:
                entregar_500 = monto // 500
            # Se sustrae la mayor cantidad de billetes de 500
            monto_restante -= entregar_500 * 500
            # Se compara residuo y existencia de los billetes de 200
            if monto_restante // 200 > self.__billetes_200:
                entregar_200 = self.__billetes_200
            else:
                entregar_200 = monto_restante // 200
            # Se sustrae la mayor cantidad de billetes de 200
            monto_restante -= entregar_200 * 200
            # Se compara residuo y existencia de los billetes de 100
            if monto_restante // 100 > self.__billetes_100:
                entregar_100 = self.__billetes_100
            else:
                entregar_100 = monto_restante // 100
            # Se sustrae la mayor cantidad de billetes de 100
            monto_restante -= entregar_100 * 100
            # Se compara residuo y existencia de los billetes de 50
            if monto_restante // 50 > self.__billetes_50:
                entregar_50 = self.__billetes_50
            else:
                entregar_50 = monto_restante // 50
            # Se sustrae la mayor cantidad de billetes de 50
            monto_restante -= entregar_50 * 50
            # Si el resto no es completo, no hay billetes para completar la operacion
            if monto_restante != 0:
                # No se expende dinero (No hay billetes para completar).
                print(f"\nNo se puede cumplir la orden.\nSe requisitó: ${monto}\nSe expende: $0")
            else:
                # Se toman los billetes para surtir la orden
                self.__billetes_1000 -= entregar_1000
                self.__billetes_500 -= entregar_500
                self.__billetes_200 -= entregar_200
                self.__billetes_100 -= entregar_100
                self.__billetes_50 -= entregar_50
                # Se entregan en pantalla y se aniade un resumen de la operacion
                print("\nSe requisitó: $", f"{monto}",
                      "\nSe expende: $", entregar_1000 * 1000 + entregar_500 * 500 + entregar_200 * 200 + entregar_100 * 100 + entregar_50 * 50,
                      "\nBilletes:",
                      bool(entregar_1000)*("\n$1000: " + str(entregar_1000)),
                      bool(entregar_500)*("\n$500: " + str(entregar_500)),
                      bool(entregar_200)*("\n$200: " + str(entregar_200)),
                      bool(entregar_100)*("\n$100: " + str(entregar_100)),
                      bool(entregar_50)*("\n$50: " + str(entregar_50)))
    

def main():
    """
    Funcion principal del sistema (Funcion de arranque o composicion).

    Parameters:
        (None): No recibe nada.
    
    Returns:
        (None): No retorna nada.
    """
    #Se instancia un objeto de la clase Cajero
    cajero = Cajero()
    # Iniciamos el sistema con mensaje de bienvenida
    print("\n--- Dispensadora de Billetes ---")
    #Ciclo para mantener el menu de arranque
    while True:
        # Solicitamos el monto requerido y se habilita el 0 como escape
        print("\nIngrese el monto a retirar (0 para salir): ")
        entrada = input()
        if entrada == "0":
            break
        flag = False
        # Validacion de entero
        for x in entrada:
            # Bandera de caracter
            flag = False
            # String con todos los digitos
            for y in "1234567890":
                # Si x esta es un digito se marca
                if x == y:
                    flag = True
                    break
            # La bandera debe ser True SIEMPRE
            if not flag:
                break
        # Logica de cajero
        if flag:
            # Transformamos el valor dato a un tipo de dato entero y retiramos el contenido
            cajero.retirar(int(entrada))
        else:
            # No se expende dinero (Monto incorrecto)
            print(f"\nMonto incorrecto.\nSe requisitó: ${entrada}\nSe expende: $0")

#Se inicia el sistema
main()
