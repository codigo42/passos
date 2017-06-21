import random

AGUA = '-'
PEDRA = '#'
SETA = 'A'


class Mapa:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.casas = [[AGUA] * largura for i in range(altura)]

    def __str__(self):
        linhas = []
        for fila in self.casas:
            linha = []
            for casa in fila:
                linha.append(casa)
            linhas.append(''.join(linha))
        return '\n'.join(linhas)

    def __getitem__(self, coord):
        y, x = coord
        return self.casas[y][x]

    def __setitem__(self, coord, valor):
        y, x = coord
        self.casas[y][x] = valor

    def construir(self):
        y0 = self.altura // 2
        x0 = self.largura // 2
        self[y0, x0] = PEDRA
        y, x = y0, x0
        while True:
            opcoes = list(self.casas_viaveis(y, x))
            if not opcoes:
                break
            y, x = random.choice(opcoes)
            self[y, x] = PEDRA
        self[y0, x0] = SETA

    @classmethod
    def ler(self, texto):
        linhas = texto.split('\n')
        altura = len(linhas)
        largura = len(linhas[0])
        mapa = Mapa(largura, altura)
        for y, linha in enumerate(linhas):
            for x, caractere in enumerate(linha):
                assert caractere in [AGUA, PEDRA]
                mapa[y, x] = caractere
        return mapa

    def ortogonais(self, y, x):
        coords = [(y-1, x), (y, x-1), (y, x+1), (y+1, x)]
        for vy, vx in coords:
            if all([vy >= 0, vx >= 0, vy < self.altura, vx < self.largura]):
                yield (vy, vx)

    def vizinhas(self, y, x, material):
        return [(vy, vx) for vy, vx in self.ortogonais(y, x)
                if self[vy, vx] == material]

    def casas_viaveis(self, y, x):
        """gerar casas viaveis para construir ao redor de (y, x)"""
        for vy, vx in self.ortogonais(y, x):
            if self[vy, vx] == AGUA and len(self.vizinhas(vy, vx, PEDRA)) == 1:
                yield (vy, vx)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        mapa = Mapa(*(int(n) for n in sys.argv[1:]))
    else:
        mapa = Mapa(7, 5)
    mapa.construir()
    print(mapa)
