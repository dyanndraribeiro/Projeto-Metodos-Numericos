# Métodos Numéricos — Projeto 1ºGQ

Problema 4 — Desempenho de algoritmos: determinação do tamanho de entrada `n`
em que os algoritmos A e B apresentam o mesmo tempo de execução, formulado
como `f(n) = 0,01·n·log2(n) − 0,08·n − 20 = 0`.

## Integrantes

- Crystal Barbosa
- Dyanndra Ribeiro
- Eduardo Malta
- Guilherme Eduardo
- Gilberto Alves

## Instalação

Clone o repositório e instale o pacote localmente (modo editável, recomendado
durante o desenvolvimento):

```bash
git clone <url-do-repositorio>
cd <pasta-do-repositorio>
pip install -e .
```

## Uso

O pacote `metodos_numericos` expõe três funções — `bissecao`, `newton` e
`secante` — cada uma implementada em seu próprio módulo, sem uso de funções
prontas de bibliotecas para determinação de raízes.

```python
from metodos_numericos import bissecao, newton, secante

def f(n):
    ...

raiz, iteracoes = bissecao(f, a, b, tol=1e-6)
```

O notebook `notebook.ipynb` importa essas funções, aplica os três métodos ao
problema e compara os resultados (raiz encontrada, número de iterações e
critério de parada).

## Critério de parada

Descrever aqui o critério adotado (ex.: `|f(x)| < 1e-6` e/ou
`|x_{k+1} - x_k| < 1e-6`, com limite de 100 iterações) e a justificativa da
escolha.

## Estrutura do repositório

```
.
├── README.md
├── pyproject.toml
├── src/
│   └── metodos_numericos/
│       ├── __init__.py
│       ├── bissecao.py
│       ├── newton.py
│       └── secante.py
└── notebook.ipynb
```
