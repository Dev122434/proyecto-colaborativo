class Calculadora():
    def __init__(self):
        self.base = 0
        self.resultado = ''

    def leerNumeros(self):
        while True:
            try:
                self.base = int(input("Potencia: "))
                break
            except Exception:
                print("Número inválido")
                continue


    def elevarPotencia(self):
        while True:
            try:
                exponente = int(input("Exponente: "))
                break
            except Exception:
                print("Exponente invalido")
                continue

        self.resultado = f'El resultado de elevar {self.base} a {exponente} es igual a {self.base ** exponente}'

    def mostrarResultado(self):
        print(self.resultado)