from abc import ABC
from abc import abstractmethod


class BaseRootFinder(ABC):
    def __init__(self, f, start_a, start_b=1, max_error=0.01, derivative=None):
        """
        Inicialização da classe.

        Args:
            f (numpy): Função para plotar o gráfico e encontrar a raiz.
            start_a (int): Ponto X inicial para procura da raiz.
            start_b (int): Ponto X final para procura da raiz.
            max_error (float): Erro máximo aceitável para X.

        """

        super()

        self.f = f
        self.start_a = start_a
        self.start_b = start_b
        self.max_error = max_error
        self.derivative = derivative

    @abstractmethod
    def start_plotting(self):
        pass
