"""Método de Newton-Raphson para determinação de raízes de f(x) = 0."""

import math

from .resultado import ResultadoRaiz


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
        Tolerância do critério de parada: |x_{k+1} - x_k| < tol.
    max_iter : int
        Número máximo de iterações (trava de segurança).

    Retorna
    -------
    ResultadoRaiz
        Em caso de falha (derivada nula, divergência, f fora do domínio,
        max_iter), `convergiu` é False e `mensagem` explica o motivo.

    Levanta
    -------
    ValueError
        Se tol <= 0 ou max_iter <= 0.
    """
    if tol <= 0 or max_iter <= 0:
        raise ValueError("tol e max_iter devem ser positivos.")

    x = float(x0)
    fx = math.nan
    k = 0
    historico = []

    try:
        fx = f(x)
        for k in range(1, max_iter + 1):
            if fx == 0:
                return ResultadoRaiz(x, fx, k - 1, True, "x já é raiz exata.", historico)

            dfx = df(x)
            if dfx == 0:
                return ResultadoRaiz(
                    x, fx, k - 1, False,
                    f"Derivada nula em x = {x:.6g}; escolha outro chute inicial.",
                    historico,
                )

            # Passo de Newton
            x_novo = x - fx / dfx
            if not math.isfinite(x_novo):
                return ResultadoRaiz(
                    x, fx, k - 1, False, "O método divergiu (x não finito).", historico
                )

            fx_novo = f(x_novo)
            erro = abs(x_novo - x)
            historico.append({"k": k, "x": x_novo, "fx": fx_novo, "erro": erro})
            x, fx = x_novo, fx_novo

            if erro < tol or fx == 0:
                return ResultadoRaiz(
                    x, fx, k, True,
                    f"Convergência alcançada: |x_(k+1) - x_k| < tol ({tol:g}).",
                    historico,
                )
    except (ValueError, ZeroDivisionError, OverflowError) as erro_calculo:
        return ResultadoRaiz(
            x, fx, len(historico), False,
            f"Falha ao avaliar f ou f' na iteração {k}: {erro_calculo}",
            historico,
        )

    return ResultadoRaiz(
        x, fx, max_iter, False,
        "Número máximo de iterações atingido sem convergência.",
        historico,
    )