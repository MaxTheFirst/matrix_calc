from enum import Enum


class MatrixType(Enum):
    VMATRIX = 'vmatrix'
    BMATRIX = 'bmatrix'


class LatexGeneration():
    @staticmethod
    def get_new_formul_block(code):
        return f'\n\\[\n{code}\n\\]\n'

    def get_numder(numder):
        if not isinstance(numder, tuple):
            return str(numder)
        text = ''
        a, b = numder
        if a < 0 or b < 0:
            text += '-'
            if a < 0:
                a = -a
            else:
                b = -b
        text += f'\\frac{{a}}{{b}}'
        return text

    def get_matrix_code(array, matrix_type=MatrixType.BMATRIX):
        matrix_type_code = matrix_type.value
        text = f'\\begin{{matrix_type_code}}\n'
