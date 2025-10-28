from calculadora_POO import Calculadora, es_flotante

class CalculadoraDos(Calculadora):
    def __init__(self, numero1 = 0, numero2 = 0):
        super().__init__(numero1, numero2)
    
    def potencia(self):
        resultado = self._numero1 ** self._numero2
        self._registrar_operacion("^", resultado)
        return resultado


def interpretar_expresion(expresion):
    for operador in ["*", "/", "+", "^"]:
        if operador in expresion:
            partes = expresion.split(operador)
            if len(partes) == 2:
                if (es_flotante(partes[0].strip()) and es_flotante(partes[1].strip())):
                    num1 = float(partes[0].strip())
                    num2 = float(partes[1].strip())
                    return num1, num2, operador
                else: 
                    return False
    if "-" in expresion and expresion.count("-") <= 2:
        partes = expresion.split("-")
        if len(partes) == 2:
                if (es_flotante(partes[0].strip()) and es_flotante(partes[1].strip())):
                    num1 = float(partes[0].strip())
                    num2 = float(partes[1].strip())
                    return num1, num2, "-"
                else: 
                    return False
        elif len(partes) == 3:
            if (es_flotante(partes[1].strip()) and es_flotante(partes[2].strip())):
                num1 = -1*float(partes[1].strip())
                num2 = float(partes[2].strip())
                return num1, num2, "-"
            else: 
                return False
    else:
        return False


def main():
    calc = CalculadoraDos()
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
        if operador == "+":
            print("Resultado:", calc.sumar())
        elif operador == "-":
            print("Resultado:", calc.restar())
        elif operador == "*":
            print("Resultado:", calc.multiplicar())
        elif operador == "/":
            print("Resultado:", calc.dividir())
        elif operador == "^":
            print("Resultado:", calc.potencia())

main()
