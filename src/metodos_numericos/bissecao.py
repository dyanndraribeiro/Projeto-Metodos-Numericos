"""Método da Bisseção para determinação de raízes de f(x) = 0."""


def bissecao(f, a, b, tol=1e-6, max_iter=100):
    """Encontra uma raiz de f em [a, b] pelo método da bisseção.

    Parâmetros
    ----------
    f : callable
        Função contínua para a qual se busca f(x) = 0.
    a, b : float
        Extremos do intervalo inicial. É necessário que f(a) e f(b)
        tenham sinais opostos (Teorema de Bolzano).
    tol : float
        Tolerância para o critério de parada (|f(x)| < tol).
    max_iter : int
        Número máximo de iterações permitido.

    Retorna
    -------
    raiz : float
        Aproximação da raiz encontrada.
    iteracoes : int
        Número de iterações realizadas até a convergência.
    """
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos.")

    # TODO: implementar o laço de bisseção.
    # A cada iteração:
    #   1. calcular o ponto médio m = (a + b) / 2
    #   2. avaliar f(m)
    #   3. verificar o critério de parada (|f(m)| < tol ou (b - a) / 2 < tol)
    #   4. substituir a ou b por m, preservando a troca de sinal
    raise NotImplementedError
