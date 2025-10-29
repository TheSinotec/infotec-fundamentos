class Calculadora:
    """
    Representa la calculadora de dos numeros

    Attributes:
        numero1 (Integer/Float): Primer numero empleado para la operacion
        numero2 (Integer/Float): Segundo numero empleado en la operacion.
        historial  (List<dict>): Historial de operaciones.
    
    Methods:
        registrar_operacion(operador, resultado): Genera un registro de operaciones llenando una lista de diccionarios.
        sumar(): Realiza la suma entre numero1 y numero2, retorna el resultado y genera historial.
        restar(): Realiza la resta entre numero1 y numero2, retorna el resultado y genera historial.
        multiplicar(): Realiza la multiplicacion entre numero1 y numero2, retorna el resultado y genera historial.
        dividir(): Realiza la divicion entre numero1 y numero2, retorna el resultado y genera historial.
        ver_historial(): Muestra el historial de operaciones acumulado.
    """

    #Se inicializan las variables en el constructor
    def __init__(self, numero1 = 0, numero2 = 0):
        """
        Parameters:
            numero1 (Integer/Float): Primer numero empleado para la operacion
            numero2 (Integer/Float): Segundo numero empleado en la operacion.
            historial  (List<dict>): Historial de operaciones.
        """
        self._numero1 = numero1
        self._numero2 = numero2
        #Se genera una lista para historial vacio
        self._historial = []
    

    """---------setter and getter---------"""
    
    @property
    #Getter de numero1
    def numero1(self):
        return self._numero1
    
    @numero1.setter
    #Setter de numero1
    def numero1(self, nuevo_numero1):
        #Se verifica tipo de dato para generar una excepcion
        if type(nuevo_numero1) in (int, float):
            self._numero1 = nuevo_numero1
        else:
            raise ValueError("Debe ser un número")
    
    @property
    #Getter de numero2
    def numero2(self):
        return self._numero2
    
    @numero2.setter
    #Setter de numero2
    def numero2(self, nuevo_numero2):
        #Se verifica tipo de dato para generar una excepcion
        if type(nuevo_numero2) in (int, float):
            self._numero2 = nuevo_numero2
        else:
            raise ValueError("Debe ser un número")

    #Metodo para generar el registro de operaciones
    def _registrar_operacion(self, operador, resultado):
        """
        Metodo que registra una operacion efectuada en la lista historial, como lista de diccionarios con el formato de {'operacion', 'resultado'}

        Parameters:
            operador (String): Un caracter que representa el simbolo de operacion.
            resultado (Int/Float): El resultado numerico de la operacion generada.
        
        Returns:
            (None): No retorna nada
        """
        #Se agrega un diccionario como registro de lista
        self._historial.append({
            "operacion": f"{self._numero1} {operador} {self._numero2}",
            "resultado": resultado
        })
    
    #Metodo para realizar la suma entre dos variables internas
    def sumar(self):
        """
        Metodo que genera la suma de numero1 y numero2.
        
        Parameters:
            (None): No recibe nada.
        
        Returns:
            resultado (Float): El resultado de la suma.
        """
        #Se suman los numeros
        resultado = self._numero1 + self._numero2
        #Se registra la operacion en el historial y se retorna el resultado
        self._registrar_operacion("+", resultado)
        return resultado
    
    #Metodo para realizar la resta entre dos variables internas
    def restar(self):
        """
        Metodo que genera la resta de numero1 y numero2.
        
        Parameters:
            (None): No recibe nada.
        
        Returns:
            resultado (Float): El resultado de la resta.
        """
        #Se restan los numeros
        resultado = self._numero1 - self._numero2
        #Se registra la operacion en el historial y se retorna el resultado
        self._registrar_operacion("-", resultado)
        return resultado
    
    #Metodo para realizar la multiplicacion entre dos variables internas
    def multiplicar(self):
        """
        Metodo que genera la multiplicacion de numero1 y numero2.
        
        Parameters:
            (None): No recibe nada.
        
        Returns:
            resultado (Float): El resultado de la multiplicacion.
        """
        #Se multiplican los numeros
        resultado = self._numero1 * self._numero2
        #Se registra la operacion en el historial y se retorna el resultado
        self._registrar_operacion("*", resultado)
        return resultado
    
    #Metodo para realizar la division entre dos variables internas
    def dividir(self):
        """
        Metodo que genera la division de numero1 y numero2.
        
        Parameters:
            (None): No recibe nada.
        
        Returns:
            resultado (Float): El resultado de la division.
        """
        #Se multiplican los numeros
        resultado = self._numero1 / self._numero2
        #Se registra la operacion en el historial y se retorna el resultado
        self._registrar_operacion("/", resultado)
        return resultado
    
    #Metodo para visualizar el historial de operaciones
    def ver_historial(self):
        """
        Metodo que muestra en pantalla el historial de las operaciones realizadas.
        
        Parameters:
            (None): No recibe nada.
        
        Returns:
            (None): No retorna nada.
        """
        #Se muestra un mensaje y escapa si el historial esta vacio
        if not self._historial:
            print("No hay operaciones en el historial.")
            return
        #Se muestra un mensaje de entarda
        print("\n--- Historial de Operaciones ---")
        contador = 1
        #Se muestran todas las operaciones en linea
        for operacion in self._historial:
            print(f"{contador}, {operacion['operacion']} = {operacion['resultado']}")
            contador += 1



#Funcion de validacion de numero flotante
def es_flotante(num: str):
    """
    Funcion que toma una cadena de texto y valida si se trata de un numero flotante.

    Parameters:
        num (String): La cadena de texto a evaluar.
    
    Returns:
        Boolean == True: Si num es un numero flotante.
        Boolean == False: Si num no es un numero flotante.
    """
    #Se valida cadena vacia
    if num == "":
        return False
    #Se agrega bandera de validacion de caracter numerico
    bandera = False
    #Se agrega contador de puntos decimales
    contador = 0
    #Se agrega contador de guiones
    guion = -1
    if (num[0] == "-"):
        guion += 1
    #Ciclo de validacion de digitos y contador de puntos decimales
    for x in num:
        #Se valida digito y un unico punto decimal
        if x in "1234567890":
            bandera = True
        elif x == "." and contador < 1:
            #Se cuentan puntos
            contador += 1
        elif x == "-" and guion < 1:
            #Se cuentan guiones
            guion += 1
        else:
            return False
    #Se valida la existencia de al menos un numero y/o el guion de negativo
    return True if bandera and (guion == 1 or guion == -1) else False

#Funcion para validar que la operacion en una expresion sea valida                   
def interpretar_expresion(expresion):
    """
    Funcion que toma una cadena de texto y valida si se trata de una operacion numerica de dos numeros validos.

    Parameters:
        expresion (String): La cadena de texto a evaluar.
    
    Returns:
        num1 (Float): El primer numero aislado de la expresion.
        num2 (Float): El segundo numero aislado de la expresion.
        operador (String): El operador que representa la operacion.
        Boolean == False: Si expresion no es una operacion valida.
    """
    #Se verifican tres de las operaciones que solo admiten un operador
    for operador in ["*", "/", "+"]:
        #Si el operador esta en la expresion 
        if operador in expresion:
            #Se divide la expresion segun el operador
            partes = expresion.split(operador)
            #Si solo existe un simbolo se validan las partes
            if len(partes) == 2:
                #Si ambas partes representan un numero se convierte a flotante y se regresan junto con el operador
                if (es_flotante(partes[0].strip()) and es_flotante(partes[1].strip())):
                    num1 = float(partes[0].strip())
                    num2 = float(partes[1].strip())
                    return num1, num2, operador
                else: 
                    #Si no son numeros
                    return False
    #Si se trata de una resta se contemplan mas de un solo signo de resta (numeros negativos)
    if "-" in expresion and expresion.count("-") <= 2:
        #Se fracciona segun el signo
        partes = expresion.split("-")
        #Si genera dos partes solo se trata de una resta
        if len(partes) == 2:
                #Se valida nuevamente si se trata de dos numeros flotantes y se regresan los numeros segmentados con su operador
                if (es_flotante(partes[0].strip()) and es_flotante(partes[1].strip())):
                    num1 = float(partes[0].strip())
                    num2 = float(partes[1].strip())
                    return num1, num2, "-"
                else: 
                    #Si no son numeros
                    return False
        #Si genera tres partes se trata de una resta a un numero negativo
        elif len(partes) == 3:
            #Se verifica que ambas partes sean numeros
            if (es_flotante(partes[1].strip()) and es_flotante(partes[2].strip())):
                num1 = -1*float(partes[1].strip())
                num2 = float(partes[2].strip())
                #Se regresan los nuemros y el operador
                return num1, num2, "-"
            else:
                #Si no son numeros
                return False
    else:
        #Si la expresion no cumple con la cantidad de guiones
        return False

#Se inicializa el algoritmo
def main():
    calc = Calculadora()
    print("Calculadora Básica. Escribe 'salir' para terminar o 'historial para ver operaciones.\n")
    while True:
        entrada = input("Ingresa la operacion (ejemplo 5 + 5): ").replace(" ","")
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
        match (operador):
            case "+":
                print("Resultado:", calc.sumar())
            case "-":
                print("Resultado:", calc.restar())
            case "*":
                print("Resultado:", calc.multiplicar())
            case "/":
                print("No se puede dividir por cero.") if calc.numero2 == float(0) else print("Resultado:", calc.dividir())

if __name__ == "__main__":
    main()
