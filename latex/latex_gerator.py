from .matrix_types import MatrixTypes


class LatexGenerator():
    @staticmethod
    def get_number_with_straples(numder):
        if numder >= 0:
            return str(numder)
        return f'({numder})'
    
    @staticmethod
    def get_new_formul_block(code):
        return f'\n\\[\n{code}\n\\]\n'
    
    @staticmethod
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
        text += f'\\frac{{{a}}}{{{b}}}'
        return text
    
    @staticmethod
    def get_matrix_code(array, matrix_type=MatrixTypes.BMATRIX):
        matrix_type_code = matrix_type.value
        text = f'\\begin{{{matrix_type_code}}}\n'
        
        for line in array:
            text += '&'.join(map(LatexGenerator.get_numder, line)) + '\\\\\n'
        text += f'\\end{{{matrix_type_code}}}\n'
        return text
    
    @staticmethod
    def get_determinant_code2(array, result):
        text = LatexGenerator.get_matrix_code(array, MatrixTypes.VMATRIX)
        text += f'={array[0][0]}\cdot {array[1][1]} - {LatexGenerator.get_number_with_straples(array[0][1])}\cdot {array[1][0]}={result}'
        return LatexGenerator.get_new_formul_block(text)
    
    @staticmethod
    def get_determinant_code3(array, minors_data, result):
        text = LatexGenerator.get_matrix_code(array, MatrixTypes.VMATRIX) + '='
        
        for key, value in enumerate(minors_data):
            element, minor = value
            if key == 0:
                text += str(element)
            else:
                text += LatexGenerator.get_number_with_straples(element)
            text += '\cdot ' + LatexGenerator.get_matrix_code(minor, MatrixTypes.VMATRIX)
            if key == 0:
                text += '-'
            elif key == 1:
                text += '+'
        text += f'={result}'
        return LatexGenerator.get_new_formul_block(text)
    
    @staticmethod
    def get_inverse_matrix_code(array, transformations, result):
        text = LatexGenerator.get_new_formul_block('A=' + LatexGenerator.get_matrix_code(array))
        first = True

        for matrix in transformations:
            matrix_text = ''
            if first:
                matrix_text += '(A|E)='
            matrix_text += LatexGenerator.get_matrix_code(matrix)
            text += LatexGenerator.get_new_formul_block(matrix_text)
        text += LatexGenerator.get_new_formul_block('A^{-1}=' + LatexGenerator.get_matrix_code(array))
        return text
        