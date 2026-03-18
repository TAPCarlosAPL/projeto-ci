from app import soma, subtracao

def test_soma():
    assert soma (2,3) == 5

def test_subtracao():
    assert subtracao (3,3) == 0

#TESTANDO FUNÇÃO DE SUBTRACAO COM NÚMEROS NEGATIVOS
def test_subtracao_negativo():
    assert subtracao (-3,3) == -6
    assert subtracao (-3,-3) == 0
    assert subtracao (3,-3) == 6
    assert subtracao(0, -3) == 3
    assert subtracao(-3, 0) == -3

#TESTANDO FUNÇÃO DE SOMA COM NÚMEROS NEGATIVOS
def test_soma_negativos():
    assert soma (-2,3) == 1
    assert soma (-2,-3) == -5
    assert soma (2,-3) == -1
    assert soma (0, -3) == -3


def test_erro_simulado():
    assert soma(2, 3) == 10, "Erro simulado para testar o pipeline!!"