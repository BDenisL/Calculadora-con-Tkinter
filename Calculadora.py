class Calculadora:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def mult(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error"