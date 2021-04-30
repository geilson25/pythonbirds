class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá! {id(self)}'

if __name__ == '__main__':
    geilson = Pessoa(nome='Geilson')
    iris = Pessoa(geilson, nome='Iris')
    print(Pessoa.cumprimentar(iris))
    print(id(iris))
    print(iris.cumprimentar())
    print(iris.nome)
    print(iris.idade)
    for filho in iris.filhos:
        print(filho.nome)