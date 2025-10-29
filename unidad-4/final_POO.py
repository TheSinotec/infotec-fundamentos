from calculadora_POO import Calculadora

class CalculadoraDos(Calculadora):
    def __init__(self, numero1 = 0, numero2 = 0, numero3 = 0):
        super().__init__(numero1, numero2)
        self._numero3 = numero3
        self.__calculadora = Calculadora()
    
    """---------setter and getter---------"""
    
    @property
    def numero3(self):
        return self._numero3
    
    @numero3.setter
    def numero3(self, nuevo_numero3):
        if type(nuevo_numero3) in (int, float):
            self._numero3 = nuevo_numero3
        else:
            raise ValueError("Debe ser un número")
    
    def _registrar_operacion(self, operador, resultado, operador2 = 0):
        self._historial.append({
            "operacion": f"{self._numero1} {operador} {self._numero2} "+ bool(operador2)*(f"{operador2} {self.numero3}"),
            "resultado": resultado
        })

    def sumar(self, num1, num2):
        self.__calculadora.numero1 = num1
        self.__calculadora.numero2 = num2
        resultado = self.__calculadora.sumar()
        return resultado
    
    def restar(self, num1, num2):
        self.__calculadora.numero1 = num1
        self.__calculadora.numero2 = num2
        resultado = self.__calculadora.restar()
        return resultado
    
    def multiplicar(self, num1, num2):
        resultado = 0
        for i in range(abs(num2)):
            resultado = self.sumar(resultado, num1)
        if (num2 > 0):
            return resultado
        else:
            return -resultado
    
    def dividir(self, num1, num2):
        if num2 == 0:
            return None
        resultado = 0
        signo1 = num1 >= 0
        signo2 = num2 >= 0
        num1 = abs(num1)
        num2 = abs(num2)
        resto = num1
        while True:
            if resto < num2:
                break
            resultado = self.sumar(resultado, 1)
            resto = self.restar(resto, num2)
        if (signo1 and signo2) or (not signo1 and not signo2):
            return resultado, (resto, num2)
        else:
            return -resultado, (-resto, num2)

    def potencia(self, num1, num2):
        if num2 == num1 == 0:
            return None
        elif num2 == 0:
            return 1
        signo2 = num2 >= 0
        num2 = abs(num2)
        resultado = 1
        for i in range(num2):
            resultado = self.multiplicar(resultado, num1)
        if (signo2):
            return resultado, (0, 1)
        else:
            return self.dividir(1, resultado)


#Función de validación de numero entero
def es_entero(num: str):
    """
    Función que toma una cadena de texto y valida si se trata de un número flotante positivo.

    Parameters:
        num (String): La cadena de texto a evaluar.
    
    Returns:
        Boolean == True: Si num es un número flotante positivo.
        Boolean == False: Si num no es un número flotante positivo.
    """
    #Se valida cadena vacía
    if num == "":
        return False
    #Se agrega bandera de validación de caracter numérico
    bandera = False
    #Se agrega contador de guiones
    guion = -1
    if (num[0] == "-"):
        guion += 1
    #Ciclo de validación de digitos y contador de guiones
    for x in num:
        #Se valida dígito y un unico punto decimal
        if x in "1234567890":
            bandera = True
        elif x == "-" and guion < 1:
            #Se cuentan guiones
            guion += 1
        else:
            return False
    #Se valida la existencia de al menos un número
    return True if bandera and (guion == 1 or guion == -1) else False

def interpretar_expresion(expresion):
    for operador in ["*", "/", "+", "^"]:
        if operador in expresion:
            partes = expresion.split(operador)
            if len(partes) == 2:
                if (es_entero(partes[0].strip()) and es_entero(partes[1].strip())):
                    num1 = int(partes[0].strip())
                    num2 = int(partes[1].strip())
                    return num1, num2, operador
                else: 
                    return False
    if "-" in expresion and expresion.count("-") <= 2:
        partes = expresion.split("-")
        if len(partes) == 2:
                if (es_entero(partes[0].strip()) and es_entero(partes[1].strip())):
                    num1 = int(partes[0].strip())
                    num2 = int(partes[1].strip())
                    return num1, num2, "-"
                else: 
                    return False
        elif len(partes) == 3:
            if (es_entero(partes[1].strip()) and es_entero(partes[2].strip())):
                num1 = -1*int(partes[1].strip())
                num2 = int(partes[2].strip())
                return num1, num2, "-"
            else: 
                return False
    else:
        return False

def obtener_lados(izquierda: str, derecha: str):
    primero = 0
    ultimo = 0
    for i in range(len(izquierda) - 1, -1, -1):
        if es_entero(izquierda[i:]):
            primero = i
        else:
            break
    for i in range(1, len(derecha)+1):
        if es_entero(derecha[:i]):
            ultimo = i
    return primero, ultimo + 1

def leer(expresion: str):
    if "^" in expresion:
        potencias = expresion.split("^")
        if len(potencias) > 3:
            print("MAL")
        for i in range(len(expresion) - 1, -1, -1):
            if expresion[i] == "^":
                primero, ultimo = obtener_lados(expresion[:i], expresion[i+1:])
                print(expresion[primero :i], expresion[i + 1:i + ultimo],"\n")
                #Potenciar
                #Recursivo a leer

def main():
    calc = CalculadoraDos()
    print("Calculadora Básica. Escribe 'salir' para terminar o 'historial para ver operaciones.\n")
    while True:
        entrada = input("Ingresa las operaciones de números enteros (ejemplo 5 + 5): ").replace(" ","")
        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break
        if entrada.strip().lower() == "historial":
            calc.ver_historial()
            continue
        leer("5112^-3783^-454")
        '''
        resultado = interpretar_expresion(entrada)
        if not resultado:
            print("Expresión no válida. Usa el formato: número operador número (ej. 5 + 5)\n")
            continue
        num1, num2, operador = resultado
        if operador == "+":
            print("Resultado:", calc.sumar(num1, num2))
        elif operador == "-":
            print("Resultado:", calc.restar(num1, num2))
        elif operador == "*":
            print("Resultado:", calc.multiplicar(num1, num2))
        elif operador == "/":
            print("Resultado:", calc.dividir(num1, num2))
        elif operador == "^":
            print("Resultado:", calc.potencia(num1, num2))
            '''

main()
