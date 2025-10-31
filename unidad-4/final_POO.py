from calculadora_POO import Calculadora

class CalculadoraDos(Calculadora):
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
        potencia(): Realiza la divicion entre numero1 y numero2, retorna el resultado y genera historial.
        ver_historial(): Muestra el historial de operaciones acumulado.
        es_entero():
        es_expresion():
        operar():
        obtener_lados():
        leer():
        calcular():
    """

    def __init__(self, numero1 = 0, numero2 = 0):
        """
        Parameters:
            numero1 (Integer/Float): Primer numero empleado para la operacion
            numero2 (Integer/Float): Segundo numero empleado en la operacion.
            historial  (List<dict>): Historial de operaciones.
        """
        #Se inicializa el constructor de la clase padre
        super().__init__(numero1, numero2)

    def sumar(self, num1, num2):
        """
        Metodo que genera la suma de dos numeros.
        
        Parameters:
            num1 (Integer): Numero primero.
            num2 (Integer): Numero segundo.
        
        Returns:
            resultado (Integer): El resultado de la suma de num1 y num2.
        """
        #Se inicializan los valores de dos numeros en la clase
        self._numero1, self._numero2  = num1, num2
        #Se llama al metodo de la clase padre para la operacion
        resultado = super().sumar()
        #Se elimina el historial de la operacion
        self._historial.pop()
        #Se regresa resultado
        return resultado
    
    def restar(self, num1, num2):
        """
        Metodo que genera la resta de dos numeros.
        
        Parameters:
            num1 (Integer): Numero primero.
            num2 (Integer): Numero segundo.
        
        Returns:
            resultado (Integer): El resultado de la resta de num1 y num2.
        """
        #Se inicializan los valores de dos numeros en la clase
        self._numero1, self._numero2  = num1, num2
        #Se llama al metodo de la clase padre para la operacion
        resultado = super().restar()
        #Se elimina el historial de la operacion
        self._historial.pop()
        #Se regresa resultado
        return resultado
    
    def multiplicar(self, num1, num2):
        """
        Metodo que genera la multiplicacion de dos numeros.
        
        Parameters:
            num1 (Integer): Numero primero.
            num2 (Integer): Numero segundo.
        
        Returns:
            resultado (Integer): El resultado de la multiplicacion de num1 y num2.
        """
        #Se inicializa en cero
        resultado = 0
        #Se realiza una suma iterada
        for i in range(abs(num2)):
            #Se llama a la funcion suma para realizar la operacion
            resultado = self.sumar(resultado, num1)
        #Validacion de signos
        if (num2 > 0):
            #Se regresa resultado
            return resultado
        else:
            #Se regresa resultado negativo
            return -resultado
    
    def dividir(self, num1, num2):
        """
        Metodo que genera la division de dos numeros.
        
        Parameters:
            num1 (Integer): Numero primero.
            num2 (Integer): Numero segundo.
        
        Returns:
            resultado (Integer): El resultado de la division de num1 y num2.
        """
        #Se omite division por cero
        if num2 == 0:
            return None
        #Se inicializa en cero 
        resultado = 0
        #Se computan los signos de los numeros
        signo1 = num1 >= 0
        signo2 = num2 >= 0
        #Se generan en valor absoluto
        num1, num2 = abs(num1), abs(num2)
        #Se genera un resto
        resto = num1
        #Bucle Do..while para algoritmo de division por resta
        while True:
            #Si el resto es menor al numero se escapa
            if resto < num2:
                break
            #Se cuenta la cantidad de veces que se resta
            resultado = self.sumar(resultado, 1)
            #Se resta un numero al otro segun su resto
            resto = self.restar(resto, num2)
        #Se validan signos para division
        if (signo1 and signo2) or (not signo1 and not signo2):
            #Se retornan resultado, y un par coordenado de (resto, base)
            return resultado, (resto, num2)
        else:
            #Si la operacion es de numeros negativos se mandan los signos
            return -resultado, (-resto, num2)

    def potencia(self, num1, num2):
        """
        Metodo que genera la potencia de dos numeros.
        
        Parameters:
            num1 (Integer): Numero primero.
            num2 (Integer): Numero segundo.
        
        Returns:
            resultado (Integer): El resultado de la potencia de num1 y num2.
        """
        #Se valida la potencia de 0^0
        if num2 == num1 == 0:
            return None
        #Se escapa para potencias de cero
        elif num2 == 0:
            #Se retornan resultado, y un par coordenado de (resto, base)
            return 1, (0, 1)
        #Se guarda el signo del exponente
        signo2 = num2 >= 0
        #Se cambia a valor absoluto
        num2 = abs(num2)
        #Se inicializa en 1
        resultado = 1
        #Bucle de productos iterativos
        for i in range(num2):
            #Se multiplican para exponenciar
            resultado = self.multiplicar(resultado, num1)
        if (signo2):
            #Se retornan resultado, y un par coordenado de (resto, base)
            return resultado, (0, 1)
        else:
            #Se retorna la exponenciacion negativa como una division
            return self.dividir(1, resultado)

    #Metodo para generar el registro de operaciones
    def _registrar_operacion(self, operacion, resultado):
        """
        Metodo que registra una operacion efectuada en la lista historial, como lista de diccionarios con el formato de {'operacion', 'resultado'}

        Parameters:
            operador (String): Un caracter que representa el simbolo de operacion.
            resultado (Int/String): El resultado numerico de la operacion generada.
        
        Returns:
            (None): No retorna nada
        """
        #Se agrega un diccionario como registro de lista
        self._historial.append({
            "operacion": f"{operacion}",
            "resultado": resultado
        })

    #Función de validación de numero entero
    def es_entero(self, num: str):
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

    def _es_expresion(self, expresion: str):
        """
        Metodo que verifica si una expresion es matematicamente correcta
        
        Parameters:
            expresion (String): La cadena de texto a evaluar.
        
        Returns:
            Boolean == True: Si la expresion es valida
            Boolean == False: Si la expresion no es valida
        """
        #Se elimina el primer signo negativo
        if expresion[0] == "-":
            expresion = expresion[1:]
        #Se descartan signos sobrantes extremos
        if expresion[-1] in "+-*/^":
            return False
        #Se separan cadenas segun el exponente
        expresion = expresion.split("^")
        #Para cada fragmento se generan particiones de cada signo
        for operacion in ["*", "/", "+"]:
            #Se vuelve a segmentar segun el operador
            expresion = [x.split(operacion) for x in expresion]
            #Se inicializa una lista vacía
            y = []
            #Se integran las sublistas contenidas en la lista principal para obtener una unica lista
            for x in expresion:
                #Simbolo de suma de listas
                y += [*x]
            #Se reasigna el contenido a expresion
            expresion = y
        #Se inicializa contador
        count = 0
        #Bucle que repasa signos negativos en los fragmentos de la lista general
        for i in range(len(expresion)):
            #Se cuentan los signos aledaños
            for x in expresion[i]:
                #Se valida la existencia de signos negativos
                if x == "-":
                    #Si son consecutivos se suman 
                    count += 1
                    #Si hay dos signos consecutivos se escapa
                    if count == 2:
                        return False
                else:
                    #Se reinicia el contador
                    count = 0
            #Se verifica que el fragmento no sea un numero entero
            if not self.es_entero(expresion[i]):
                #Se rectifican las partes generadas al abrir la expresion por el signo
                for x in expresion[i].split("-"):
                    #Si cada parte no es un numero se escapa
                    if not self.es_entero(x):
                        return False
            #Si el framnento es vacio se escapa
            if expresion[i] == "":
                return False
        #Se mantiene la integridad de la expresion
        return True
    
    def _operar(self, expresion: str, operador: str, i: int):
        """
        Metodo que realiza una operacion puntual entre dos numeros
        
        Parameters:
            expresion (String): La cadena de texto a evaluar.
            operador (String): El simbolo de la operacion.
            i (Integer): El indice de la posición del carácter.
        
        Returns:
            (None): Si la operacion no es posible.
            (list<String>): Si la expresion no es entera retorna la operacion simbolica.
            (String): La expresion reformulada con el resultado de la operacion.
        """
        #Se inicializan dos indices en cero
        primero, ultimo = 0, 0
        #Se obtienen los indices laterales de la particion
        primero, ultimo = self._obtener_lados(expresion[:i], expresion[i+1:])
        #Se realiza la operacion segun su operador
        match operador:
            case "^":
                resultado = self.potencia(int(expresion[primero :i]), int(expresion[i + 1:i + ultimo]))
            case "*":
                resultado = self.multiplicar(int(expresion[primero :i]), int(expresion[i + 1:i + ultimo]))
            case "/":
                resultado = self.dividir(int(expresion[primero :i]), int(expresion[i + 1:i + ultimo]))
            case "+":
                resultado = self.sumar(int(expresion[primero :i]), int(expresion[i + 1:i + ultimo]))
            case "-":
                resultado = self.restar(int(expresion[primero :i]), int(expresion[i + 1:i + ultimo]))
        #Se verifica que sea una operacion sin pie a ser fraccionaria
        if operador in "*+-":
            #Se genera el resultado en pantalla
            print(f"El resultado de {expresion[primero :i]}{operador}{expresion[i + 1:i + ultimo]} = {resultado}")
            #Se regresa la expresión nueva de la operacion realizada
            return expresion[:primero] + f"{resultado if resultado >= 0 else resultado}" + expresion[i + ultimo:]
        #Se verifica que sea una operacion con pie a ser fraccionaria
        elif operador in "^/":
            #Se valida si el resultado es una indefinicion
            if resultado == None:
                #Se manda mensaje segun el tipo de indefinicion y regresa None
                print("No se puede dividir por cero.") if operador == "/" else print("No se puede realizar esta operación")
                return None
            #Se verifica que la parte fraccionaria sea existente
            if resultado[1][0] != 0:
                #Se manda el mensaje de advertencia y se interrumpe la operacion
                print(f"La operación no es entera: \nEl resultado de {expresion[primero :i]}{operador}{expresion[i + 1:i + ultimo]} =" 
                    + bool(resultado[0])*str(resultado[0]) + f" {resultado[1][0] if resultado[1][0] < 0 else resultado[1][0]}/{resultado[1][1]}")
                print("Se interrumpe el proceso.\n")
                #Se manda la expresion truncada en una lista para validar casos
                return [(expresion[:primero] + f"{resultado[1][0] if resultado[1][0] < 0 else resultado[1][0]}/{resultado[1][1]}" + expresion[i + ultimo:])]
            else:
                #SI la parte fraccionaria es nula, se manda el resultado de la operacion
                print(f"El resultado de {expresion[primero :i]}{operador}{expresion[i + 1:i + ultimo]} = {resultado[0]}")
                #Se regresa la expresión nueva de la operacion realizada
                return expresion[:primero] + f"{resultado[0] if resultado[0] >= 0 else resultado[0]}" + expresion[i + ultimo:]
                    

    def _obtener_lados(self, izquierda: str, derecha: str):
        """
        Metodo que obtiene los numeros por la izquierda y la derecha de un par de cadenas, respectivamente.
        
        Parameters:
            izquierda (String): La cadena de la cual se toma el primer numero hacia la izquierda.
            derecha (String): La cadena de la cual se toma el primer numero hacia la derecha.
        
        Returns:
            primero (Integer): El indice izquierdo.
            ultimo + 1 (Integer): El indice derecho.
        """
        #Se inicializan dos indices en cero
        primero, ultimo = 0, 0
        #Se recorre el lado izquierdo desde la derecha
        for i in range(len(izquierda) - 1, -1, -1):
            #Se verifica que sea un entero valido
            if self.es_entero(izquierda[i:]):
                #Se registra el indice si es un entero valido
                primero = i
            else:
                #Se cierra cuando la subcadena no es un numero entero
                break
        #Se recorre el lado derecho desde la izquierda
        for i in range(1, len(derecha)+1):
            #Se verifica que sea un entero valido
            if self.es_entero(derecha[:i]):
                ultimo = i
                #Se registra el indice si es un entero valido
        #Se regresan ambos indices y se ajusta el derecho por desface de range
        return primero, ultimo + 1

    def _leer(self, expresion: str):
        """
        Metodo que realiza recursivamente las operaciones de una expresion matematica.
        
        Parameters:
            expresion (String): La cadena de texto que representa una expresion matematica.
        
        Returns:
            (Recursive) => leer(expresion)
            expresion == None: Si la operacion es indefinida 
            expresion == expresion: Si la operacion finaliza con un resultado
        """
        #Se valida expresion None indefinida
        if expresion == None:
            return expresion
        #Se valida que la expresion sea un entero resultado final
        if self.es_entero(expresion):
            return expresion
        else:
            #Se generan mensajes de desarrollo segun la expresion empleada
            print("\nExpresion actual: " + expresion)
        #Se validan potencias primero
        if "^" in expresion:
            #Ciclo de busqueda de operador de derecha a izquierda
            for i in range(len(expresion) - 1, -1, -1):
                #Si se encuentra el operador, se opera
                if expresion[i] == "^":
                    #Se realiza la operacion
                    operacion = self._operar(expresion, "^", i)
                    #Se regresa el resultado si se trunca la operación o se llama recursivamente la funcion
                    return operacion[0] if type(operacion) == list else self._leer(operacion)
        #Se validan multiplicaciones y divisiones segundo
        elif "*" in expresion or "/" in expresion:
            #Ciclo de busqueda de operador
            for i in range(len(expresion)):
                #Si se encuentra el operador, se opera
                if expresion[i] == "*":
                    #Se realiza la operacion
                    operacion = self._operar(expresion, "*", i)
                    #Se llama recursivamente la funcion
                    return self._leer(operacion)
                if expresion[i] == "/":
                    #Se realiza la operacion
                    operacion = self._operar(expresion, "/", i)
                    #Se regresa el resultado si se trunca la operación o se llama recursivamente la funcion
                    return operacion[0] if type(operacion) == list else self._leer(operacion)
        #Se validan sumas y restas al final
        elif "+" in expresion or "-" in expresion:
            #Ciclo de busqueda de operador
            for i in range(len(expresion)):
                #Si se encuentra el operador, se opera
                if expresion[i] == "+":
                    #Se realiza la operacion
                    operacion = self._operar(expresion, "+", i)
                    #Se llama recursivamente la funcion
                    return self._leer(operacion)
                #Si se encuentra el operador y no es el inicio, se opera
                if expresion[i] == "-" and i != 0:
                    #Se realiza la operacion
                    operacion = self._operar(expresion, "-", i)
                    #Se llama recursivamente la funcion
                    return self._leer(operacion)

    def calcular(self, expresion):
        """
        Metodo que realiza el calculo y validacion de una entrada de texto.
        
        Parameters:
            expresion (String): La cadena de texto a evaluar.
        
        Returns:
            (None): No retorna nada.
        """
        #Se valida que el parametro sea una expresion
        if self._es_expresion(expresion):
            #Si es una expresion se calcula el resultado
            resultado = self._leer(expresion)
            #Se validan resultados indefinidos o normales
            if resultado == None:
                #Se muestra mensaje y se guarda en historial
                print("\nRESULTADO => INDEFINIDO")
                self._registrar_operacion(expresion, "Indefinido")
            else:
                #Se muestra mensaje y se guarda en historial
                print(f"\nRESULTADO => {expresion} = {resultado}")
                self._registrar_operacion(expresion, resultado)
        else:
            #Si la operacion es incorrecta se muestra mensaje
            print("\nSYNTAX ERROR: Debe colocar una expresión matemática correcta.\nLas operaciones permitidas son [+, -, *, /, ^]")

#Funcion de arranque
if __name__ == "__main__":
    #Se instancia CalculadoraDos
    calc = CalculadoraDos()
    #mensaje de entrada
    print("Calculadora Básica. Escribe 'salir' para terminar o 'historial para ver operaciones.\n")
    #Se cicla el menu
    while True:
        #Se pide una expresion
        entrada = input("Ingresa las operaciones de números enteros (ejemplo 5 + 5): ").replace(" ","")
        #Se vaida escape
        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break
        #Se valida funcion de historial
        if entrada.strip().lower() == "historial":
            calc.ver_historial()
            print("\n")
            continue
        #Se pasa la expresión en la calculadora
        calc.calcular(entrada)
