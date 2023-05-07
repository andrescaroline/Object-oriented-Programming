# classe de produtos e aplicação de descontos


class produto:
    def __init__(self, ied, preco_mercado, desconto):
        self.ied = ied
        self.preco_mercado = preco_mercado
        self.desconto = desconto

    @property
    def preco_venda(self):
        return self.preco_mercado - 0.01 * self.desconto * self.preco_mercado

    def mostrar(self):
        print(self.ied, self.preco_mercado, self.desconto)

    @property
    def desconto(self):
        return self._desconto+2 if self.preco_mercado > 500 else self._desconto
    
    @desconto.setter
    def desconto(self, novo_desconto):
        self._desconto = novo_desconto


c1 = produto('AID2', 100, 5)
c2 = produto('AED3',200, 10)
c3 = produto('AOD4', 1000, 20)

c3.mostrar()