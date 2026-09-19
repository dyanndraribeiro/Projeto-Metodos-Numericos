def newton_raphson(f, df, a, b, tol=1e-3, max_iter=100):
    # Verifica se o intervalo [a, b] contém uma raiz, utilizando o Teorema do Valor Intermediário de Bolzano
   
    if f(a) * f(b) >= 0:
        return False, None ,"o intervalo [a, b] não contém uma raiz, pois f(a) e f(b) têm o mesmo sinal."

    x0 = (a + b) / 2  # Chute inicial como o ponto médio do intervalo
    contador = 0

    while True: 
        # Calcula o valor da função e sua derivada no ponto atual
        fx0 = f(x0)
        dfx0 = df(x0)

        # Verifica se a derivada é muito próxima de zero para evitar divisão por zero
        if (abs(dfx0) < 1e-10):
            return False, None, "A derivada é muito próxima de zero no ponto inicial, escolha outro intervalo."
        
        # Aplica o método de Newton-Raphson para saber o próximo ponto
        x1 = x0 - fx0 / dfx0

        # Verifica se o método divergiu, ou seja, se o próximo ponto está muito longe do ponto atual
        if (x1 > 1e10) or (x1 < -1e10):
            return False, None, "O método divergiu, escolha outro intervalo."
        
        # Verifica se a convergência foi alcançada
        if (abs(x1 - x0) < tol) or (abs(f(x1)) < tol):
            return True, x1, f"Convergência alcançada na iteração {contador + 1}."

        # Atualiza o ponto atual e incrementa o contador de iterações para motivos de trava de segurança
        x0 = x1
        contador += 1

        # Verfica se o numero de iterações atingiu o limite, evitando loops sem término
        if contador >= max_iter:
            return False, None, "Número máximo de iterações atingido sem convergência."


