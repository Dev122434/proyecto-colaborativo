from math import sqrt

class Calculadora():
    def __init__(self):
        self.base = 0
        self.resultado = ''

    def elevarPotencia(self):
        while True:
            try:
                self.base = int(input("Número: "))
                break
            except Exception:
                print("Número inválido")
                continue
        while True:
            try:
                exponente = int(input("Exponente: "))
                break
            except Exception:
                print("Exponente invalido")
                continue

        self.resultado = f'El resultado de elevar {self.base} a {exponente} es igual a {self.base ** exponente}'
        print(self.resultado)


    def calcularRaizCuadrada(self):
        while True:
            try:
                self.base = float(input("Número para raíz cuadrada: "))
                if self.base < 0:
                    print("No se puede calcular la raíz cuadrada de un número negativo.")
                    continue
                break
            except Exception:
                print("Número inválido")
                continue

        self.resultado = f'La raíz cuadrada de {self.base} es {sqrt(self.base)}'
        print(self.resultado)