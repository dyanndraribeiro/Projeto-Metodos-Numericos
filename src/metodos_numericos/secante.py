"""Método da Secante para determinação de raízes de f(x) = 0."""


def secante(f, x0, x1, tol=1e-6, max_iter=100):
    """Encontra uma raiz de f pelo método da secante.

    Parâmetros
    ----------
    f : callable
        Função para a qual se busca f(x) = 0.
    x0, x1 : float
        Dois chutes iniciais (não é necessário que tenham sinais opostos).
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
    # TODO: implementar o laço da secante.
    # A cada iteração:
    #   1. calcular x_{k+1} = x_k - f(x_k) * (x_k - x_{k-1}) /
    #                          (f(x_k) - f(x_{k-1}))
    #   2. tratar o caso f(x_k) - f(x_{k-1}) == 0
    #   3. verificar o critério de parada (|f(x_{k+1})| < tol ou
    #      |x_{k+1} - x_k| < tol)
    raise NotImplementedError
