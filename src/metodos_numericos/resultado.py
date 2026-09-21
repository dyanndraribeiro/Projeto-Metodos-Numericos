"""Estrutura de resultado padronizada, compartilhada pelos três métodos."""

from dataclasses import dataclass, field


@dataclass
class ResultadoRaiz:
    """Resultado devolvido por `bissecao`, `newton` e `secante`.

    Atributos
    ---------
    raiz : float
        Melhor aproximação da raiz obtida.
    f_raiz : float
        Valor de f na raiz aproximada.
    iteracoes : int
        Número de iterações realizadas.
    convergiu : bool
        True se o critério de parada foi satisfeito; False se o método
        falhou (max_iter atingido, derivada nula, f indefinida etc.).
    mensagem : str
        Descrição de como o método terminou.
    historico : list[dict]
        Uma entrada por iteração, com as chaves "k", "x", "fx" e "erro"
        (a bisseção acrescenta "a" e "b"). "erro" é o erro estimado usado
        no critério de parada.
    """

    raiz: float
    f_raiz: float
    iteracoes: int
    convergiu: bool
    mensagem: str
    historico: list = field(default_factory=list)

    @property
    def erro_estimado(self):
        """Erro estimado da última iteração (0.0 se não houve iterações)."""
        return self.historico[-1]["erro"] if self.historico else 0.0