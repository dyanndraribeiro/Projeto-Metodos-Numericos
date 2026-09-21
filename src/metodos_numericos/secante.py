"""Método da Secante para determinação de raízes de f(x) = 0."""

import math

from .resultado import ResultadoRaiz


def secante(f, x0, x1, tol=1e-6, max_iter=100):
    """Encontra uma raiz de f pelo método da secante.

    A cada iteração:
        x_{k+1} = x_k - f(x_k) * (x_k - x_{k-1}) / (f(x_k) - f(x_{k-1}))

    Parâmetros
    ----------
    f : callable
        Função para a qual se busca f(x) = 0.
    x0, x1 : float
        Dois chutes iniciais distintos (não precisam ter sinais opostos).
    tol : float
        Tolerância do critério de parada: |x_{k+1} - x_k| < tol.
    max_iter : int
        Número máximo de iterações (trava de segurança).

    Retorna
    -------
    ResultadoRaiz
        Em caso de falha (f(x_k) = f(x_{k-1}), divergência, f fora do
        domínio, max_iter), `convergiu` é False e `mensagem` explica o motivo.

    Levanta
    -------
    ValueError
        Se x0 == x1, tol <= 0 ou max_iter <= 0.
    """
    if x0 == x1:
        raise ValueError("x0 e x1 devem ser distintos.")
    if tol <= 0 or max_iter <= 0:
        raise ValueError("tol e max_iter devem ser positivos.")

    x_ant, x = float(x0), float(x1)
    f_ant = math.nan
    fx = math.nan
    k = 0
    historico = []

    try:
        f_ant, fx = f(x_ant), f(x)
        for k in range(1, max_iter + 1):
            if fx == 0:
                return ResultadoRaiz(x, fx, k - 1, True, "x já é raiz exata.", historico)

            denominador = fx - f_ant
            if denominador == 0:
                return ResultadoRaiz(
                    x, fx, k - 1, False,
                    "f(x_k) = f(x_(k-1)): a reta secante é horizontal.",
                    historico,
                )

            # Passo da secante
            x_novo = x - fx * (x - x_ant) / denominador
            if not math.isfinite(x_novo):
                return ResultadoRaiz(
                    x, fx, k - 1, False, "O método divergiu (x não finito).", historico
                )

            fx_novo = f(x_novo)
            erro = abs(x_novo - x)
            historico.append({"k": k, "x": x_novo, "fx": fx_novo, "erro": erro})
            x_ant, f_ant = x, fx
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
            f"Falha ao avaliar f na iteração {k}: {erro_calculo}",
            historico,
        )

    return ResultadoRaiz(
        x, fx, max_iter, False,
        "Número máximo de iterações atingido sem convergência.",
        historico,
    )