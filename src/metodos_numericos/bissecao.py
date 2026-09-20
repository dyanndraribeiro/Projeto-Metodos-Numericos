"""Método da Bisseção para determinação de raízes de f(x) = 0."""

from .resultado import ResultadoRaiz


def bissecao(f, a, b, tol=1e-6, max_iter=100):
    """Encontra uma raiz de f em [a, b] pelo método da bisseção.

    Parâmetros
    ----------
    f : callable
        Função contínua para a qual se busca f(x) = 0.
    a, b : float
        Extremos do intervalo inicial (a < b), com f(a) e f(b) de sinais
        opostos.
    tol : float
        Tolerância do critério de parada: o método para quando
        (b - a) / 2 < tol, o que garante erro menor que tol na raiz.
    max_iter : int
        Número máximo de iterações (trava de segurança).

    Retorna
    -------
    ResultadoRaiz

    Levanta
    -------
    ValueError
        Se a >= b, tol <= 0, max_iter <= 0 ou se f(a) e f(b) têm o mesmo
        sinal (sem garantia de raiz no intervalo).
    """
    if a >= b:
        raise ValueError("O intervalo deve satisfazer a < b.")
    if tol <= 0 or max_iter <= 0:
        raise ValueError("tol e max_iter devem ser positivos.")

    fa = f(a)
    fb = f(b)

    # Se uma das extremidades já é raiz, não há necessidade de iterar
    if fa == 0:
        return ResultadoRaiz(a, 0.0, 0, True, "A extremidade a já é raiz.")
    if fb == 0:
        return ResultadoRaiz(b, 0.0, 0, True, "A extremidade b já é raiz.")

    # Teorema do Valor Intermediário (Bolzano): precisa haver troca de sinal
    if (fa > 0) == (fb > 0):
        raise ValueError(
            "f(a) e f(b) têm o mesmo sinal: não há garantia de raiz em [a, b]."
        )

    historico = []
    for k in range(1, max_iter + 1):
        # Ponto médio e valor da função nele
        c = a + (b - a) / 2
        fc = f(c)
        # Após k passos, |c - raiz| <= (b - a) / 2 (intervalo atual)
        erro = (b - a) / 2
        historico.append({"k": k, "a": a, "b": b, "x": c, "fx": fc, "erro": erro})

        if fc == 0 or erro < tol:
            return ResultadoRaiz(
                c, fc, k, True,
                f"Convergência alcançada: erro estimado < tol ({tol:g}).",
                historico,
            )

        # Mantém a metade onde ainda há troca de sinal:
        # c substitui o extremo que tem o mesmo sinal de f(c)
        if (fa > 0) != (fc > 0):
            b = c
        else:
            a = c
            fa = fc

    return ResultadoRaiz(
        c, fc, max_iter, False,
        "Número máximo de iterações atingido sem convergência.",
        historico,
    )