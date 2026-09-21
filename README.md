# Métodos Numéricos — Projeto 1ºGQ

Problema 4 — Desempenho de algoritmos: determinação do tamanho de entrada `n`
em que os algoritmos A e B apresentam o mesmo tempo de execução, formulado
como `f(n) = 0,01·n·log2(n) − 0,08·n − 20 = 0`, com

- `T_A(n) = 0,01·n·log2(n)`
- `T_B(n) = 0,08·n + 20`

## Integrantes

- Crystal Barbosa
- Dyanndra Ribeiro
- Eduardo Malta
- Guilherme Eduardo
- Gilberto Alves

## Instalação

Requer Python 3.9 ou superior. Clone o repositório e instale o pacote
localmente:

```bash
git clone https://github.com/dyanndraribeiro/Projeto-Metodos-Numericos.git
cd Projeto-Metodos-Numericos
pip install -e .
```

Para executar o notebook (instala também `jupyter` e `matplotlib`):

```bash
pip install -e ".[notebook]"
jupyter notebook notebook.ipynb
```

Para rodar os testes automatizados:

```bash
pip install -e ".[test]"
pytest
```

## Uso

O pacote `metodos_numericos` expõe três funções, cada uma em seu próprio
módulo e implementada pelo grupo, **sem uso de funções prontas de bibliotecas
para determinação de raízes**. As três devolvem um objeto `ResultadoRaiz`.

| Método | Assinatura | Entradas específicas |
|---|---|---|
| Bisseção | `bissecao(f, a, b, tol=1e-6, max_iter=100)` | intervalo `[a, b]` com troca de sinal |
| Newton-Raphson | `newton(f, df, x0, tol=1e-6, max_iter=100)` | derivada `df` e chute inicial `x0` |
| Secante | `secante(f, x0, x1, tol=1e-6, max_iter=100)` | dois chutes iniciais distintos |

```python
import math
from metodos_numericos import bissecao, newton, secante

def f(n):
    return 0.01 * n * math.log2(n) - 0.08 * n - 20

def df(n):
    return 0.01 * (math.log2(n) + 1 / math.log(2)) - 0.08

r = bissecao(f, 500, 2000, tol=1e-6)
print(r.raiz, r.iteracoes, r.convergiu)   # 1010.01724... 31 True

r = newton(f, df, 1250)
r = secante(f, 500, 2000)
```

Campos de `ResultadoRaiz`:

| Campo | Significado |
|---|---|
| `raiz` | melhor aproximação da raiz |
| `f_raiz` | valor de `f` na raiz aproximada |
| `iteracoes` | número de iterações realizadas |
| `convergiu` | `True` se o critério de parada foi satisfeito |
| `mensagem` | como o método terminou (ou o motivo da falha) |
| `historico` | lista de dicionários, uma entrada por iteração (`k`, `x`, `fx`, `erro`; a bisseção inclui também `a` e `b`) |

Entradas inválidas (`a >= b`, `tol <= 0`, intervalo sem troca de sinal etc.)
levantam `ValueError`. Falhas numéricas durante a iteração (derivada nula,
divergência, `f` fora do domínio, `max_iter` atingido) não levantam exceção:
retornam `convergiu = False` com a explicação em `mensagem`.

O notebook `notebook.ipynb` importa essas funções, aplica os três métodos ao
problema e compara os resultados (raiz, erro, iterações, tempo e convergência).

## Critério de parada e precisão

**Precisão adotada:** `tol = 1e-6` (em unidades de `n`), a mesma nos três
métodos, para que a comparação seja justa. Limite de segurança: `max_iter = 100`.

| Método | Critério | Garantia |
|---|---|---|
| Bisseção | `(b − a) / 2 < tol` | erro na raiz **menor que `tol`** (garantido) |
| Newton | `abs(x_{k+1} − x_k) < tol` | estimativa do erro |
| Secante | `abs(x_{k+1} − x_k) < tol` | estimativa do erro |

**Justificativas**

- **Escala do problema:** a raiz é `n ≈ 1010`, então `1e-6` equivale a uma precisão
  relativa de cerca de `1e-9`.
- **Decisão para `n` inteiro:** a raiz (`≈ 1010,0172`) fica a 0,017 do inteiro 1010 e
  a 0,983 do 1011. Qualquer erro muito menor que 0,017 já decide a questão, e
  `1e-6` dá uma folga de quatro ordens de grandeza.
- **Custo baixo:** a bisseção precisa de `⌈log2((b − a)/tol)⌉ = 31` iterações
  em `[500, 2000]`. O limite de 100 é folgado, mesmo para `tol = 1e-10` (44 iterações).
- **Por que não usar `|f(x)| < tol`:** perto da raiz `f'(n) ≈ 0,034`, então
  `|f| < tol` aceitaria um `n` com erro cerca de 30 vezes maior que `tol`
  (`|Δn| ≈ |f| / f'`). Nos testes com o critério em `|f|`, a bisseção parou com erro
  real de `2,9e-5` para `tol = 1e-6`. Por isso o critério é sempre sobre `x`.
- **Newton e secante:** convergem superlinearmente, então o erro real do último
  iterado costuma ser bem menor que o passo `|x_{k+1} − x_k|`; o critério é
  uma estimativa conservadora.

## Resultado

- Raiz: `n* ≈ 1010,0172`.
- O algoritmo **A** tem o menor tempo para `1 ≤ n ≤ 1010`.
- O algoritmo **B** tem o menor tempo para `n ≥ 1011`.
- Não há inteiro com tempos iguais: `f(1010) ≈ −0,0006` e `f(1011) ≈ +0,0336`.

Detalhes, tabelas e gráficos estão no notebook.

## Estrutura do repositório

```
.
├── README.md
├── pyproject.toml
├── src/
│   └── metodos_numericos/
│       ├── __init__.py
│       ├── resultado.py     # dataclass ResultadoRaiz
│       ├── bissecao.py
│       ├── newton.py
│       └── secante.py
├── tests/
│   └── test_metodos.py
└── notebook.ipynb
```