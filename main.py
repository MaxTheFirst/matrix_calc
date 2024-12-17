from window import window
import callbacks

from calcs import DeterminantCalc
from latex import LatexGenerator

import tkinter as tk

def main():
    array22 = [[[1, (-2, 5)], [3, 4]], [[1, 2], [3, 4]]]
    array33 = [[1, -2, 3], [4, 5, 6], [7, 8, 9]]

    print(LatexGenerator.get_inverse_matrix_code(array33, array22, array33))
    
if __name__ == "__main__":
    main()
