class VerificadorBalanceo:
    def __init__(self, expresion: str):
        self.expresion = expresion
        self.pila = []
        self.pares = {')': '(', '}': '{', ']': '['}


    def verificar_balanceo(self):
        for caracter in self.expresion:
            if caracter in '({[':
                self.pila.append(caracter)
            elif caracter in ')}]':
                if not self.pila or self.pila.pop() != self.pares[caracter]:
                    return False
        return not self.pila
    
    def __str__(self):
        return f'La expresión {self.expresion} está balanceada: {self.verificar_balanceo()}'    
    

expresion1 = VerificadorBalanceo('[{()}]')
print(expresion1)
expresion2 = VerificadorBalanceo(']')
print(expresion2)