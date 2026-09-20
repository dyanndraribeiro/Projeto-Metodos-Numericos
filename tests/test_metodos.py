"""Testes dos três métodos. Execute com:  pytest"""

import math

import pytest

from metodos_numericos import bissecao, newton, secante

# Problema 4: f(n) = T_A(n) - T_B(n)
RAIZ_REF = 1010.0172448799  # referência obtida com alta precisão


def f(n):
    return 0.01 * n * math.log2(n) - 0.08 * n - 20


def df(n):
    return 0.01 * (math.log2(n) + 1 / math.log(2)) - 0.08


# ---------------------------------------------------------------- bisseção
def test_bissecao_raiz_de_2():
    r = bissecao(lambda x: x**2 - 2, 1, 2, tol=1e-8)
    assert r.convergiu
    assert abs(r.raiz - math.sqrt(2)) < 1e-8


def test_bissecao_problema_erro_menor_que_tol():
    r = bissecao(f, 500, 2000, tol=1e-6)
    assert r.convergiu
    assert abs(r.raiz - RAIZ_REF) < 1e-6  # garantia de erro < tol


def test_bissecao_numero_de_iteracoes_previsto():
    # k >= log2((b - a) / tol) = log2(1500 / 1e-6) ~ 30,5  ->  31
    r = bissecao(f, 500, 2000, tol=1e-6)
    assert r.iteracoes == 31
    assert len(r.historico) == 31


def test_bissecao_raiz_na_extremidade():
    r = bissecao(lambda x: x - 1, 1, 3)
    assert r.convergiu and r.raiz == 1 and r.iteracoes == 0


def test_bissecao_sem_mudanca_de_sinal():
    with pytest.raises(ValueError):
        bissecao(f, 1100, 2000)


def test_bissecao_entradas_invalidas():
    with pytest.raises(ValueError):
        bissecao(f, 2000, 500)  # a > b
    with pytest.raises(ValueError):
        bissecao(f, 500, 2000, tol=0)
    with pytest.raises(ValueError):
        bissecao(f, 500, 2000, max_iter=0)


def test_bissecao_max_iter_devolve_ultima_aproximacao():
    r = bissecao(f, 500, 2000, tol=1e-12, max_iter=10)
    assert not r.convergiu
    assert r.raiz is not None and r.iteracoes == 10


# ------------------------------------------------------------------ newton
def test_newton_problema():
    r = newton(f, df, 1250, tol=1e-6)
    assert r.convergiu
    assert abs(r.raiz - RAIZ_REF) < 1e-6
    assert r.iteracoes <= 5


def test_newton_derivada_nula():
    r = newton(lambda x: x**2 + 1, lambda x: 2 * x, 0)
    assert not r.convergiu and "Derivada nula" in r.mensagem


def test_newton_fora_do_dominio():
    # de x0 = 50 o passo de Newton cai em n < 0, onde log2 não existe
    r = newton(f, df, 50)
    assert not r.convergiu


def test_newton_entradas_invalidas():
    with pytest.raises(ValueError):
        newton(f, df, 1250, tol=-1)


# ----------------------------------------------------------------- secante
def test_secante_problema():
    r = secante(f, 500, 2000, tol=1e-6)
    assert r.convergiu
    assert abs(r.raiz - RAIZ_REF) < 1e-6


def test_secante_reta_horizontal():
    r = secante(lambda x: x**2 - 4, -1, 1)  # f(-1) = f(1)
    assert not r.convergiu and "horizontal" in r.mensagem


def test_secante_entradas_invalidas():
    with pytest.raises(ValueError):
        secante(f, 500, 500)


# --------------------------------------------------------------- consistência
def test_tres_metodos_concordam():
    rb = bissecao(f, 500, 2000, tol=1e-6).raiz
    rn = newton(f, df, 1250, tol=1e-6).raiz
    rs = secante(f, 500, 2000, tol=1e-6).raiz
    assert abs(rb - rn) < 1e-5 and abs(rb - rs) < 1e-5


def test_decisao_para_n_inteiro():
    assert f(1010) < 0 < f(1011)  # A menor até 1010; B menor a partir de 1011