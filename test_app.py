from app import soma, saudacao

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

from app import soma, saudacao, multiplicacao

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6

def test_saudacao():
    resultado = saudacao("Mundo")
    assert "Mundo" in resultado
    assert resultado.startswith("Olá")
