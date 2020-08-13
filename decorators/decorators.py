'''
O QUE É?
Decorator, é um padrão de projeto de software que permite 
adicionar um comportamento a um objeto já existente em tempo 
de execução, ou seja, agrega dinamicamente responsabilidades 
adicionais a um objeto.
'''
class uppercase(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        self.func(args[0].upper())


@uppercase
def nome(nome):
    print(f"Nome:{nome}")

'''
Chamando a função nome() e passando um argumento lowcase observamos que
ao utilizar o decorator @uppercase o resultado é alterado para upper
'''
nome("jean")
