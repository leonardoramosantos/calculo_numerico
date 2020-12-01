from imports import START_X_AXYS
from imports import END_X_AXYS
from imports import SAMPLES_X_AXYS
from imports import ROUND_FLOATS

from BaseRootFinder import BaseRootFinder


class BisectionRootFinder(BaseRootFinder):
    """
    Classe que contém o código para encontrar a Raiz de uma função.

    Criada classe para reutilização de código.

    """

    def start_plotting(self):
        """
        Início da função para buscar a raiz.

        Args:
            Todos os parâmetros já foram introduzidos na inicialização da
            classe.

        """

        print("")
        print("###############################################################################################")
        print("#     A      #     XM     #     B      #     F(A)    #     F(XM)   #    F(B)    #     ERRO    #")
        print("###############################################################################################")

        self.recursive_find_root(self.start_a, self.start_b, 10)

    def recursive_find_root(self, a, b, current_loop):
        """
        Função recursiva para encontrar a raiz da função escolhida.

        Args:
            a (float): Ponto a para buscar a raiz.
            b (float): Ponto b para buscar a raiz.
            current_loop (int): Loop atual. Cada recursão, subtrai 1 do loop.
                Quando chega a 0, sai do programa para evitar loop infinito.

        """

        xm = (b + a) / 2
        error = b - xm

        a_pos = ((a - START_X_AXYS) * SAMPLES_X_AXYS /
                 (END_X_AXYS - START_X_AXYS))
        b_pos = ((b - START_X_AXYS) * SAMPLES_X_AXYS /
                 (END_X_AXYS - START_X_AXYS))
        xm_pos = ((xm - START_X_AXYS) * SAMPLES_X_AXYS /
                  (END_X_AXYS - START_X_AXYS))

        str_output = "#{} #{} #{} #{} #{} #{} #{} #".format(
            str(round(a, ROUND_FLOATS)).rjust(11),
            str(round(xm, ROUND_FLOATS)).rjust(11),
            str(round(b, ROUND_FLOATS)).rjust(11),
            str(round(self.f[int(a_pos)], ROUND_FLOATS)).rjust(12),
            str(round(self.f[int(xm_pos)], ROUND_FLOATS)).rjust(12),
            str(round(self.f[int(b_pos)], ROUND_FLOATS)).rjust(12),
            str(round(error, ROUND_FLOATS)).rjust(12))

        print(str_output)

        ascendente = a_pos < b_pos

        a_to_xm = True if self.f[int(xm_pos)] < 0 else False
        if ascendente:
            a_to_xm = False if self.f[int(xm_pos)] < 0 else True

        if (error > self.max_error) and (current_loop > 0):
            next_a = a if a_to_xm else xm
            next_b = xm if a_to_xm else b

            self.recursive_find_root(next_a, next_b, current_loop - 1)
