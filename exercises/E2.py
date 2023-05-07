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

    def em_estoque(self):
        if self.copias > 0:
            return True
        else:
            False
    
    def alugar(self):
        if self.em_estoque:
            self.copias -= 1
        else:
            print('livro está fora de estoque!')


livro1 = livro('Learn phisycs','957-4-36-547417-1', 'Stephen', 'CBC', 350, 200, 10)
livro2 = livro('Learn Chemistry','652-6-86-748413-3', 'Jack', 'CBC', 400, 220,20)
livro3 = livro('Learn Maths', '957-7-39-347216-2', 'John', 'XYZ', 500, 300,5)
livro4 = livro('Learn Biology', '957-7-39-347216-2', 'Jack', 'XYZ', 400, 200,6)

#livro1.mostrar()
#livro2.mostrar()
##livro4.mostrar()

#livro1.em_estoque()

#livro3.alugar()
#livro3.alugar()
#livro3.alugar()
#livro3.alugar()
#livro3.alugar()
#livro3.alugar()

# visualização por meio de listas
livros = [livro1, livro2, livro3, livro4]

for i in livros:
    i.mostrar()

# encontrando livros de jack e adicionando a lista.

jack_books = []

for e in livros:
    if e.autor =='Jack':
        jack_books.append(e.titulo)

print(jack_books)

