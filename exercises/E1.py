class contabank:
    def __init__(self, name, poupanca):
        self.name = name
        self.poupanca = poupanca
         
    def deposito(self, valor):
        self.poupanca += valor

    def saque(self, saque):
        self.poupanca -= saque

    def mostrar(self):
        print(self.name, self.poupanca)


a1 = contabank('Andresa', 200)
a2 = contabank('caroline', 300)
a3 = contabank('silva', 50)

a1.mostrar()
a2.mostrar()
a3.mostrar()


a1.deposito(20)
a2.saque(50)
a3.deposito(15)

a1.mostrar()
a2.mostrar()
a3.mostrar()
              
        


