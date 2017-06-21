from caminho import Mapa, PEDRA


def test_mapa_zerado():
    assert str(Mapa(4, 3)) == '~~~~\n~~~~\n~~~~'


def test_mapa_ler():
    texto = ('~~~~\n'
             '~~~~\n'
             '~~~~')
    mapa = Mapa.ler(texto)
    assert mapa.largura == 4
    assert mapa.altura == 3
    assert str(mapa) == texto


def test_ortogonais_centro():
    mapa = Mapa.ler('~~~\n'
                    '~#~\n'
                    '~~~')
    assert list(mapa.ortogonais(1, 1)) == [(0, 1), (1, 0), (1, 2), (2, 1)]


def test_ortogonais_lado_esq():
    mapa = Mapa.ler('~~~\n'
                    '#~~\n'
                    '~~~')
    assert list(mapa.ortogonais(1, 0)) == [(0, 0), (1, 1), (2, 0)]


def test_ortogonais_canto_sup_esq():
    mapa = Mapa.ler('#~\n'
                    '~~')
    assert list(mapa.ortogonais(0, 0)) == [(0, 1), (1, 0)]


def test_ortogonais_canto_inf_esq():
    mapa = Mapa.ler('~~\n'
                    '#~')
    assert list(mapa.ortogonais(1, 0)) == [(0, 0), (1, 1)]


def test_vizinhas_canto_inf_esq_isolada():
    mapa = Mapa.ler('~~\n'
                    '#~')
    assert list(mapa.vizinhas(1, 0, PEDRA)) == []


def test_vizinhas_canto_inf_esq_1_vizinha():
    mapa = Mapa.ler('#~\n'
                    '#~')
    assert list(mapa.vizinhas(1, 0, PEDRA)) == [(0, 0)]


def test_vizinhas_canto_inf_esq_2_vizinhas():
    mapa = Mapa.ler('#~\n'
                    '##')
    assert list(mapa.vizinhas(1, 0, PEDRA)) == [(0, 0), (1, 1)]


def test_vizinhas_lado_esq_3_vizinhas():
    mapa = Mapa.ler('#~~\n'
                    '##~\n'
                    '#~~')
    assert list(mapa.vizinhas(1, 0, PEDRA)) == [(0, 0), (1, 1), (2, 0)]


def test_viaveis_canto_inf_esq_com_vizinho():
    mapa = Mapa.ler('~~\n'
                    '##')
    assert list(mapa.casas_viaveis(1, 0)) == [(0, 0)]


def test_viaveis_canto_inf_esq_com_2_vizinhos():
    mapa = Mapa.ler('#~\n'
                    '##')
    assert list(mapa.casas_viaveis(1, 0)) == []


def test_viaveis_centro_com_vizinho():
    mapa = Mapa.ler('~~~\n'
                    '~##\n'
                    '~~~')
    assert list(mapa.casas_viaveis(1, 1)) == [(0, 1), (1, 0), (2, 1)]


def test_viaveis_centro_com_2_vizinhos():
    mapa = Mapa.ler('~#~\n'
                    '~##\n'
                    '~~~')
    assert list(mapa.casas_viaveis(1, 1)) == [(1, 0), (2, 1)]


def test_viaveis_centro_com_vizinho_diagonal():
    mapa = Mapa.ler('~~#\n'
                    '~##\n'
                    '~~~')
    assert list(mapa.casas_viaveis(1, 1)) == [(1, 0), (2, 1)]


def test_viaveis_centro_com_2_vizinhos_diagonais():
    mapa = Mapa.ler('~~#\n'
                    '~#~\n'
                    '~~#')
    assert list(mapa.casas_viaveis(1, 1)) == [(1, 0)]


def test_viaveis_centro_com_2_vizinhos_diagonais_sem_opcao():
    mapa = Mapa.ler('#~~\n'
                    '~#~\n'
                    '~~#')
    assert list(mapa.casas_viaveis(1, 1)) == []
