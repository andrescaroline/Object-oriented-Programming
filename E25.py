# modo para chamar um atributo global é: 'nomedaclass'.atributo
class Vendedores:

    #atributo global
    receita_total = 0
    nomes = []

    def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade
      self.qtd_vendas = 0 # atributo mutável sem estar no init, nao sei ainda o motivo.
      Vendedores.nomes.append(nome)

    def fazer_venda(self, dinheiro):
      self.qtd_vendas += dinheiro
      Vendedores.receita_total += dinheiro

    def mostrar(self):
       print('nome: {}, idade: {}, total: {}' .format(self.nome, self.idade, self.qtd_vendas))


v1 = Vendedores('andresa', 22)
v2 = Vendedores('caroline', 21)
v3 = Vendedores('dea', 24)

v1.fazer_venda(2000)
v2.fazer_venda(50)
v3.fazer_venda(300)

v1.mostrar()
v2.mostrar()
v3.mostrar()

print(Vendedores.receita_total) # total de vendas de todos os vendedores.
print(Vendedores.nomes)