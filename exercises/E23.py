# class fração
# isinstance e uma função que retorna true se o objeto especificado for do tipo especificado.
# tipo recebe: A type or a class, or a tuple of types and/or classes

class fracao:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr

        if self.dr < 0:
            self.dr *= -1
            self.nr *= -1

    def mostrar(self):
        print(f'{self.nr}/{self.dr}')

    def multiplicar(self, other):
        if isinstance(other, int):
            other = fracao(other)
        return fracao(nr)(self.nr * other.nr , self.dr * other.dr)

    
    def add(self, other):
        if isinstance(other,int):
            other = fracao(other)
        return fracao(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)

       


f1 = fracao(2,3)
f1.mostrar()
f2 = fracao(2,-3)
f2.mostrar()

f1.add('2')
f1.mostrar()