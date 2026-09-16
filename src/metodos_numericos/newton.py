"""Método de Newton-Raphson para determinação de raízes de f(x) = 0."""


def newton(f, df, x0, tol=1e-6, max_iter=100):
    """Encontra uma raiz de f pelo método de Newton-Raphson.

    Parâmetros
    ----------
    f : callable
        Função para a qual se busca f(x) = 0.
    df : callable
        Derivada de f.
    x0 : float
        Chute inicial.
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
    # TODO: implementar o laço de Newton-Raphson.
    # A cada iteração:
    #   1. calcular x_{k+1} = x_k - f(x_k) / df(x_k)
    #   2. tratar o caso df(x_k) == 0 (derivada nula) com um erro claro
    #   3. verificar o critério de parada (|f(x_{k+1})| < tol ou
    #      |x_{k+1} - x_k| < tol)
    raise NotImplementedError
