from Number import Number
import numpy as np
from scipy.linalg import *
def get_answer(ordinary_matrix, inverse_matrix):
    n, m = ordinary_matrix.shape
    kol = 0
    for i in range(n):
        for j in range(m):
            kol = max(kol, len(str(ordinary_matrix[i][j])), len(str(inverse_matrix[i][j])))
    for i in range(n):
        print('(', end = ' ')
        for j in range(m):
            element = str(ordinary_matrix[i][j])
            print(element, end = ' ' * (kol - len(element) + 1))
        print('|', end = ' ')
        for j in range(m):
            element = str(inverse_matrix[i][j])
            print(element, end = ' ' * (kol - len(element) + 1))
        print(')')
    print()
class Matrix:
    def __init__(self, new_matrix):
        self._array = np.array(new_matrix, copy = True)
        self._lines, self._columns = self._array.shape
        self.__fl = np.full((self._lines, self._columns), 0.0)
        for i in range(self._lines):
            for j in range(self._columns):
                self.__fl[i][j] = float(self._array[i][j])
    def __getitem__(self, index):
        return Matrix(self._array[index])
    def __str__(self):
        answer = ""
        kol = 0
        for i in range(self._lines):
            for j in range(self._columns):
                kol = max(kol, len(str(self._array[i][j])))
        for i in range(self._lines):
            answer += "( "
            for j in range(self._columns):
                answer += str(self._array[i][j]) + ' ' * (kol - len(str(self._array[i][j])) + 1)
            answer += ')\n'
        answer += '\n'
        return answer
    def get_number_of_lines(self):
        return self._lines
    def get_number_of_columns(self):
        return self._columns
    def get_determinant(self):
        return det(self.__fl)
    def get_inverse_matrix(self):
        if self._lines != self._columns or det(self.__fl) == 0.0:
            raise ValueError("Некорректное значение")
        inverse_matrix = np.full((self._lines, self._columns), Number("0"))
        for i in range(self._lines):
            inverse_matrix[i][i] = Number("1")
        ordinary_matrix = np.array(self._array, copy = True)
        for i in range(self._lines):
            if ordinary_matrix[i][i] == Number("0"):
                for j in range(i, self._lines):
                    if ordinary_matrix[j][i] != Number("0"):
                        ordinary_matrix[i] += ordinary_matrix[j]
                        inverse_matrix[i] += inverse_matrix[j]
                        break
            if ordinary_matrix[i][i] != Number("1"):
                inverse_matrix[i] /= ordinary_matrix[i][i]
                ordinary_matrix[i] /= ordinary_matrix[i][i]
            for j in range(self._lines):
                if j == i:
                    continue
                inverse_matrix[j] -= inverse_matrix[i] * ordinary_matrix[j][i]
                ordinary_matrix[j] -= ordinary_matrix[i] * ordinary_matrix[j][i]
        return Matrix(inverse_matrix)
    def get_inverse_matrix_with_comment(self):
        if self._lines != self._columns or det(self.__fl) == 0.0:
            raise ValueError("Некорректное значение")
        inverse_matrix = np.full((self._lines, self._columns), Number("0"))
        for i in range(self._lines):
            inverse_matrix[i][i] = Number("1")
        ordinary_matrix = np.array(self._array, copy = True)
        for i in range(self._lines):
            if ordinary_matrix[i][i] == Number("0"):
                for j in range(i, self._lines):
                    if ordinary_matrix[j][i] != Number("0"):
                        ordinary_matrix[i] += ordinary_matrix[j]
                        inverse_matrix[i] += inverse_matrix[j]
                        get_answer(ordinary_matrix, inverse_matrix)
                        break
            if ordinary_matrix[i][i] != Number("1"):
                inverse_matrix[i] /= ordinary_matrix[i][i]
                ordinary_matrix[i] /= ordinary_matrix[i][i]
                get_answer(ordinary_matrix, inverse_matrix)
            for j in range(self._lines):
                if j == i or ordinary_matrix[j][i] == Number("0"):
                    continue
                inverse_matrix[j] -= inverse_matrix[i] * ordinary_matrix[j][i]
                ordinary_matrix[j] -= ordinary_matrix[i] * ordinary_matrix[j][i]
                get_answer(ordinary_matrix, inverse_matrix)
        return Matrix(inverse_matrix)

class Matrix2(Matrix):
    def __init__(self, new_matrix):
        super().__init__(new_matrix)
        if self._lines != self._columns or self._lines != 2:
            raise ValueError("Некорректное значение")
    def get_determinant(self):
        return self._array[0][0] * self._array[1][1] - self._array[0][1] * self._array[1][0]
    def get_float_determinant(self):
        return float(self.get_determinant())
    def get_inverse_matrix(self):
        if self.get_determinant() == Number("0"):
            raise ValueError("Некорректное значение")
        divider = Number("1") / self.get_determinant()
        inverse_matrix = np.array(self._array, copy = True)
        inverse_matrix[0][0], inverse_matrix[1][1] = inverse_matrix[1][1], inverse_matrix[0][0]
        inverse_matrix[0][1] *= Number("-1")
        inverse_matrix[1][0] *= Number("-1")
        for i in range(self._lines):
            for j in range(self._columns):
                inverse_matrix[i][j] *= divider
        return Matrix(inverse_matrix)
    def get_inverse_matrix_with_comment(self):
        if self.get_determinant() == Number("0"):
            raise ValueError("Некорректное значение")
        divider = Number("1") / self.get_determinant()
        inverse_matrix = np.array(self._array, copy = True)
        inverse_matrix[0][0], inverse_matrix[1][1] = inverse_matrix[1][1], inverse_matrix[0][0]
        inverse_matrix[0][1] *= Number("-1")
        inverse_matrix[1][0] *= Number("-1")
        kol = 0
        for i in range(self._lines):
            for j in range(self._columns):
               kol = max(kol, len(str(self._array[i][j])))
        print(divider, " * ( ", inverse_matrix[0][0], ' ' * (kol - len(str(inverse_matrix[0][0])) + 1),
              inverse_matrix[0][1], ' ' * (kol - len(str(inverse_matrix[0][1])) + 1), ')', sep = "")
        print(' ' * (len(str(divider)) + 3), "( ", inverse_matrix[1][0], ' ' * (kol - len(str(inverse_matrix[1][0])) + 1),
              inverse_matrix[1][1], ' ' * (kol - len(str(inverse_matrix[1][1])) + 1), ')', sep = "")
        print()
        for i in range(self._lines):
            for j in range(self._columns):
                inverse_matrix[i][j] *= divider
        return Matrix2(inverse_matrix)

class Matrix3(Matrix):
    def __init__(self, new_matrix):
        super().__init__(new_matrix)
        if self._lines != self._columns or self._lines != 3:
            raise ValueError("Некорректное значение")
    def get_determinant(self):
        main_diagonal = Number("0")
        for i in range(self._columns):
            work = Number("1")
            for j in range(3):
                work *= self._array[j][(i + j) % 3]
            main_diagonal += work
        secondary_diagonal = Number("0")
        for i in range(self._columns):
            work = Number("-1")
            for j in range(3):
                work *= self._array[j][((i - j) % 3 + 3) % 3]
            secondary_diagonal += work
        return main_diagonal + secondary_diagonal
    def get_float_determinant(self):
        return float(self.get_determinant())











