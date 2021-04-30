"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade  de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade;
2) Método acelerar, que deverá incrementar a velocidade de uma unidade;
3) Método frear que deverá decrementar a velocidade em duas unidades.

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste;
2) Método dirar_a_direita;
3) Método dirar_a_esquerda;

    N
O       L
    S

    Exemplo:
    # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> # Testando direção
    >>> direcao = Direcao()
    >>> diracao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> diracao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> diracao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> diracao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> diracao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> diracao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> diracao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> diracao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> diracao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro_calcular_velocidade()
    0
    >>> carro_acelerar()
    >>> carro_calcular_velocidade()
    1
    >>> carro_acelerar()
    >>> carro_calcular_velocidade()
    2
    >>> carro_frear()
    >>> carro_calcular_velocidade()
    0
    >>> carro.calcular_diracao()
    >>> 'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_diracao()
    >>> 'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_diracao()
    >>> 'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_diracao()
    >>> 'Oeste'
"""
class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)