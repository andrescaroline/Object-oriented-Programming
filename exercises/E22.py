class livro:
    def __init__(self, titulo, isbn, autor, editora, paginas, preco, copias):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.editora = editora
        self.preco = preco 
        self.copias = copias
        self.paginas = paginas

    def mostrar(self):
        print(self.titulo)
        print('ISBN: {}' .format(self.isbn))
        print('Preço: {}'.format(self.preco))
        print('Números de copias: {}'.format(self.copias))
        print('.' * 50)

    @property
    def preco(self):
        return self._preco

    @preco.setter  #padroes de restrições de atributo.
    def preco(self, novo_preco):
        if 10 <= novo_preco <= 500:
            self._preco = novo_preco
        else:
            raise ValueError('Price cannot be less than 10 or more than 500')




livro1 = livro('Learn phisycs','957-4-36-547417-1', 'Stephen', 'CBC', 350, 10, 7)
livro2 = livro('Learn Chemistry','652-6-86-748413-3', 'Jack', 'CBC', 400, 220,20)
livro3 = livro('Learn Maths', '957-7-39-347216-2', 'John', 'XYZ', 500, 300,5)
livro4 = livro('Learn Biology', '957-7-39-347216-2', 'Jack', 'XYZ', 400, 200,6)

livro1.mostrar()
livro2.mostrar()
livro3.mostrar()
livro4.mostrar()

# se o valor do livro não estiver dentro da restrição, ele não instancia

a = livro1.copias == livro2.copias
print(a)