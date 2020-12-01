from BaseRootFinder import BaseRootFinder

from imports import START_X_AXYS
from imports import END_X_AXYS
from imports import SAMPLES_X_AXYS
from imports import ROUND_FLOATS


class NewtonRootFinder(BaseRootFinder):
    """
    Classe que contém o código que calcula a raiz de uma função pelo método
    Newton Raphson.

    """

    def start_plotting(self):
        iteraction = 1

        print("#######################################################################")
        print("#      ITER K #       XK    #    F(XK)    #   F'(XK)    #     ERRO    #")

        self.recursive_find_root(iteraction, self.start_a)
        print("#######################################################################")

    def recursive_find_root(self, iteraction, curr_a):
        a_pos = int((curr_a - START_X_AXYS) * SAMPLES_X_AXYS /
                    (END_X_AXYS - START_X_AXYS)) - 1

        f_val = self.f[a_pos]
        f_d_val = self.derivative[a_pos]
        erro = abs(f_val)

        print("# {} # {} # {} # {} # {} #".format(
                str(iteraction).rjust(11),
                str(round(curr_a, ROUND_FLOATS)).rjust(11),
                str(round(f_val, ROUND_FLOATS)).rjust(11),
                str(round(f_d_val, ROUND_FLOATS)).rjust(11),
                str(round(erro, ROUND_FLOATS)).rjust(11)))

        if erro >= self.max_error:
            next_a = curr_a - (f_val / f_d_val)

            self.recursive_find_root(iteraction + 1, next_a)
