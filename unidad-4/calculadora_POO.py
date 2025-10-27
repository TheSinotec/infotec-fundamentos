class Calculadora:
    """
    Representa la calculadora de dos numeros

    Attributes:
        numero1 (Integer/Float): Primer numero empleado para la operacion
        numero2 (Integer/Float): Segundo numero empleado en la operacion.
        historial  (List<dict>): Historial de operaciones.
    
    Methods:
        registrar_operacion(operador, resultado): 
    """
    def __init__(self, numero1 = 0, numero2 = 0):
        self._numero1 = numero1
        self._numero2 = numero2
        self._historial = []
    
    """---------setter and getter---------"""
    @property
    def numero1(self):
        return self._numero1
    
    @numero1.setter
    def numero1(self, nuevo_numero1):
        if type(nuevo_numero1) in (int, float):
            self._numero1 = nuevo_numero1
        else:
            raise ValueError("Debe ser un número")
    
    @property
    def numero2(self):
        return self._numero2
    
    @numero2.setter
    def numero2(self, nuevo_numero2):
        if type(nuevo_numero2) in (int, float):
            self._numero2 = nuevo_numero2
        else:
            raise ValueError("Debe ser un número")

    def _registrar_operacion(self, operador, resultado):
        self._historial.append({
            "operacion": f"{self._numero1} {operador} {self._numero2}",
            "resultado": resultado
        })

    def sumar(self):
        resultado = self._numero1 + self._numero2
        self._registrar_operacion("+", resultado)
        return resultado
    
    def restar(self):
        resultado = self._numero1 - self._numero2
        self._registrar_operacion("-", resultado)
        return resultado
    
    def multiplicar(self):
        resultado = self._numero1 * self._numero2
        self._registrar_operacion("*", resultado)
        return resultado
    
    def dividir(self):
        resultado = self._numero1 / self._numero2
        self._registrar_operacion("/", resultado)
        return resultado
    
    def ver_historial(self):
        if not self._historial:
            print("No hay operaciones en el historial.")
            return
        print("\n--- Historial de Operaciones ---")
        contador = 1
        for operacion in self._historial:
            print(f"{contador}, {operacion['operacion']} = {operacion['resultado']}")
            contador += 1



#Función de validación de numero flotante
def es_flotante(num: str):
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
    return True if bandera else False

#No jala xd    
def interpretar_expresion(expresion):
    for operador in ["+", "-", "*", "/"]:
        if operador in expresion:
            partes = expresion.split(operador)
            if len(partes) == 2:
                if (es_flotante(partes[0].strip()) and es_flotante(partes[1].strip())):
                    num1 = float(partes[0].strip())
                    num2 = float(partes[1].strip())
                    return num1, num2, operador
                else: 
                    return False
                
def main():
    calc = Calculadora()
    print("Calculadora Básica. Escribe 'salir' para terminar o 'historial para ver operaciones.\n")
    while True:
        entrada = input("Ingresa la operacion (ejemplo 5 + 5): ")
        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break
        if entrada.strip().lower() == "historial":
            calc.ver_historial()
            continue
        resultado = interpretar_expresion(entrada)
        if not resultado:
            print("Expresión no válida. Usa el formato: número operador número (ej. 5 + 5)\n")
            continue
        num1, num2, operador = resultado
        calc.numero1 = num1
        calc.numero2 = num2
        if operador == "+":
            print("Resultado:", calc.sumar())
        elif operador == "-":
            print("Resultado:", calc.restar())
        elif operador == "*":
            print("Resultado:", calc.multiplicar())
        elif operador == "/":
            print("Resultado:", calc.dividir())

main()
