from calculadora_POO import Calculadora

class CalculadoraDos(Calculadora):
    def __init__(self, numero1 = 0, numero2 = 0):
        super().__init__(numero1, numero2)
        self._expresion_anterior = ""

    def sumar(self, num1, num2):
        self._numero1 = num1
        self._numero2 = num2
        resultado = super().sumar()
        return resultado
    
    def restar(self, num1, num2):
        self._numero1 = num1
        self._numero2 = num2
        resultado = super().restar()
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

    #Metodo para generar el registro de operaciones
    def _registrar_operacion(self, operacion, resultado):
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
        if expresion[0] == "-":
            expresion = expresion[1:]
        if expresion[-1] in "+-*/^":
            return False
        expresion = expresion.split("^")
        for operacion in ["*", "/", "+"]:
            expresion = [x.split(operacion) for x in expresion]
            y=[]
            for x in expresion:
                y+=[*x]
            expresion = y
        count = 0
        for i in range(len(expresion)):
            for x in expresion[i]:
                if x == "-":
                    count += 1
                    if count == 2:
                        return False
                else:
                    count = 0
            if not self.es_entero(expresion[i]):
                for x in expresion[i].split("-"):
                    if not self.es_entero(x):
                        return False
            if expresion[i] == "":
                return False
        return True
    
    def _operar(expresion: str, operador: str, i: int, fraccional: bool):
        if fraccional:
            pass
        else:
            pass

    def _obtener_lados(self, izquierda: str, derecha: str):
        primero = 0
        ultimo = 0
        for i in range(len(izquierda) - 1, -1, -1):
            if self.es_entero(izquierda[i:]):
                primero = i
            else:
                break
        for i in range(1, len(derecha)+1):
            if self.es_entero(derecha[:i]):
                ultimo = i
        return primero, ultimo + 1

    def _leer(self, expresion: str):
        if self.es_entero(expresion):
            return expresion
        else:
            print("\nExpresion actual: " + expresion)
        if "^" in expresion:
            for i in range(len(expresion) - 1, -1, -1):
                if expresion[i] == "^":
                    primero, ultimo = 0, 0
                    primero, ultimo = self._obtener_lados(expresion[:i], expresion[i+1:])
                    resultado = self.potencia(int(expresion[primero :i]), int(expresion[i + 1:i + ultimo]))
                    if resultado[1][0] != 0:
                        print(f"La potencia no es entera: \nEl resultado de {expresion[primero :i]}^{expresion[i + 1:i + ultimo]} =" 
                            + bool(resultado[0])*str(resultado[0]) + f" {resultado[1][0] if resultado[1][0] < 0 else resultado[1][0]}/{resultado[1][1]}")
                        print("Se interrumpe el proceso.\n")
                        return (expresion[:primero] + f"{resultado[1][0] if resultado[1][0] < 0 else resultado[1][0]}/{resultado[1][1]}" + expresion[i + ultimo:])
                    else:
                        print(f"El resultado de {expresion[primero :i]}^{expresion[i + 1:i + ultimo]} = {resultado[0]}")
                        return self._leer(expresion[:primero] + f"{resultado[0] if resultado[0] >= 0 else resultado[0]}" + expresion[i + ultimo:])
        elif "*" in expresion or "/" in expresion:
            for i in range(len(expresion)):
                if expresion[i] == "*":
                    primero, ultimo = 0, 0
                    primero, ultimo = self._obtener_lados(expresion[:i], expresion[i+1:])
                    resultado = self.multiplicar(int(expresion[primero :i]), int(expresion[i + 1:i + ultimo]))
                    print(f"El resultado de {expresion[primero :i]}*{expresion[i + 1:i + ultimo]} = {resultado}")
                    return self._leer(expresion[:primero] + f"{resultado if resultado >= 0 else resultado}" + expresion[i + ultimo:])
                if expresion[i] == "/":
                    primero, ultimo = 0, 0
                    primero, ultimo = self._obtener_lados(expresion[:i], expresion[i+1:])
                    resultado = self.dividir(int(expresion[primero :i]), int(expresion[i + 1:i + ultimo]))
                    if resultado == None:
                        print("No se puede dividir por cero.")
                        return None
                    if resultado[1][0] != 0:
                        print(f"La division no es entera: \nEl resultado de {expresion[primero :i]}/{expresion[i + 1:i + ultimo]} =" 
                            + bool(resultado[0])*str(resultado[0]) + f" {resultado[1][0] if resultado[1][0] < 0 else resultado[1][0]}/{resultado[1][1]}")
                        print("Se interrumpe el proceso.\n")
                        return (expresion[:primero] + f"{resultado[1][0] if resultado[1][0] < 0 else resultado[1][0]}/{resultado[1][1]}" + expresion[i + ultimo:])
                    else:
                        print(f"El resultado de {expresion[primero :i]}/{expresion[i + 1:i + ultimo]} = {resultado[0]}")
                        return self._leer(expresion[:primero] + f"{resultado[0] if resultado[0] >= 0 else resultado[0]}" + expresion[i + ultimo:])
        elif "+" in expresion or "-" in expresion:
            for i in range(len(expresion)):
                if expresion[i] == "+":
                    primero, ultimo = 0, 0
                    primero, ultimo = self._obtener_lados(expresion[:i], expresion[i+1:])
                    resultado = self.sumar(int(expresion[primero :i]), int(expresion[i + 1:i + ultimo]))
                    print(f"El resultado de {expresion[primero :i]}+{expresion[i + 1:i + ultimo]} = {resultado}")
                    return self._leer(expresion[:primero] + f"{resultado if resultado >= 0 else resultado}" + expresion[i + ultimo:])
                if expresion[i] == "-" and i != 0:
                    primero, ultimo = 0, 0
                    primero, ultimo = self._obtener_lados(expresion[:i], expresion[i+1:])
                    resultado = self.restar(int(expresion[primero :i]), int(expresion[i + 1:i + ultimo]))
                    print(f"El resultado de {expresion[primero :i]}-{expresion[i + 1:i + ultimo]} = {resultado}")
                    return self._leer(expresion[:primero] + f"{resultado if resultado >= 0 else resultado}" + expresion[i + ultimo:])

    def calcular(self, expresion):
        if self._es_expresion(expresion):
            resultado = self._leer(expresion)
            if resultado == None:
                print("\nRESULTADO => INDEFINIDO")
                self._registrar_operacion(expresion, "Indefinido")
            else:
                print(f"\nRESULTADO => {expresion} = {resultado}")
                self._registrar_operacion(expresion, resultado)
        else:
            print("\nSYNTAX ERROR: Debe colocar una expresión matemática correcta.\nLas operaciones permitidas son [+, -, *, /, ^]")

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
        calc.calcular(entrada)

main()
