class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá, meu nome é {(self.nome)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai} (Aperto de mão).'

class Mulher(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pai = Pessoa.cumprimentar(self)
        return f'{cumprimentar_da_classe_pai} (Aperto de mão).'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    geilson = Mutante(nome='Geilson')
    iris = Mulher(geilson, nome='Iris')
    print(Pessoa.cumprimentar(iris))
    print(id(iris))
    print(iris.cumprimentar())
    print(iris.nome)
    print(iris.idade)
    for filho in iris.filhos:
        print(filho.nome)
    iris.sobrenome = 'Fidelis'
    del iris.filhos
    iris.olhos = 1
    del iris.olhos
    print(iris.__dict__)
    print(geilson.__dict__)
    print(Pessoa.olhos)
    print(iris.olhos)
    print(geilson.olhos)
    print(id(Pessoa.olhos), id(iris.olhos), id(geilson.olhos))
    print(Pessoa.metodo_estatico(), iris.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), iris.nome_e_atributos_de_classe())
    pessoa=Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(geilson, Pessoa))
    print(isinstance(geilson, Homem))
    print(isinstance(iris, Pessoa))
    print(isinstance(iris, Mulher))
    print(geilson.olhos)
    print(iris.cumprimentar())
    print(geilson.cumprimentar())