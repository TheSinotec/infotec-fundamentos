from calculadora_POO import Calculadora

class CalculadoraDos(Calculadora):
    def __init__(self, numero1 = 0, numero2 = 0):
        super().__init__(numero1, numero2)
    
    def potencia(self):
        resultado = self._numero1 ** self._numero2
        self._registrar_operacion("^", resultado)
        return resultado
