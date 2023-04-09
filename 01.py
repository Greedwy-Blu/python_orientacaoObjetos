class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura


controle = ControleRemoto('azul', 10, 4, 6)

print(controle.cor)

