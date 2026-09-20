def bissecao(f, a, b, tol=1e-6, max_iter=100):
    # Calcula o valor da função nas extremidades do intervalo [a, b]
    fa = f(a)
    fb = f(b)

    # Se uma das extremidades já é raiz, não há necessidade de iterar
    if fa == 0:
        return True, a, "A extremidade a do intervalo já é uma raiz."
    if fb == 0:
        return True, b, "A extremidade b do intervalo já é uma raiz."

    # Verifica se o intervalo [a, b] contém uma raiz, utilizando o Teorema do Valor Intermediário de Bolzano
    if fa * fb > 0:
        return False, None, "O intervalo [a, b] não contém uma raiz, pois f(a) e f(b) têm o mesmo sinal."

    contador = 0

    while True:
        # Calcula o ponto médio do intervalo atual e o valor da função nele
        m = (a + b) / 2
        fm = f(m)

        # Verifica se a convergência foi alcançada: função quase nula ou intervalo suficientemente pequeno
        if (abs(fm) < tol) or ((b - a) / 2 < tol):
            return True, m, f"Convergência alcançada na iteração {contador + 1}."

        # Descarta a metade do intervalo que não contém a raiz, mantendo a troca de sinal entre as extremidades
        if fa * fm < 0:
            b = m
        else:
            a = m
            fa = fm

        # Incrementa o contador de iterações para motivos de trava de segurança
        contador += 1

        # Verifica se o número de iterações atingiu o limite, evitando loops sem término
        if contador >= max_iter:
            return False, None, "Número máximo de iterações atingido sem convergência."