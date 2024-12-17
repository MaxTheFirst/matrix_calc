from .matrix_types import MatrixTypes


class LatexGenerator():
    @staticmethod
    def normalize_number(number):
        return '%g' % round(number, 6)
    
    @staticmethod
    def normalize_array(array):
        return list(map(lambda i: list(map(LatexGenerator.normalize_number, i)), array))
    
    @staticmethod
    def get_number_with_straples(number):
        str_number = LatexGenerator.normalize_number(number)
        if number >= 0:
            return str_number
        return f'({str_number})'
    
    @staticmethod
    def get_new_formul_block(code):
        return f'\n\\[\n{code}\n\\]\n'
    
    @staticmethod
    def get_number(number):
        if not isinstance(number, tuple):
            return LatexGenerator.normalize_number(number)
        text = ''
        a, b = number
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
            text += '&'.join(map(LatexGenerator.get_number, line)) + '\\\\\n'
        text += f'\\end{{{matrix_type_code}}}\n'
        return text
    
    @staticmethod
    def get_determinant_code2(array, result):
        text = LatexGenerator.get_matrix_code(array, MatrixTypes.VMATRIX)
        text += '={}\cdot {} - {}\cdot {}={}'.format(
            LatexGenerator.normalize_number(array[0][0]),
            LatexGenerator.get_number_with_straples(array[1][1]),
            LatexGenerator.get_number_with_straples(array[0][1]),
            LatexGenerator.get_number_with_straples(array[1][0]),
            LatexGenerator.normalize_number(result)
        )
        return LatexGenerator.get_new_formul_block(text)
    
    @staticmethod
    def get_determinant_code3(array, minors_data, result):
        text = LatexGenerator.get_matrix_code(array, MatrixTypes.VMATRIX) + '='
        
        for key, value in enumerate(minors_data):
            element, minor = value
            if key == 0:
                text += LatexGenerator.normalize_number(element)
            else:
                text += LatexGenerator.get_number_with_straples(element)
            text += '\cdot ' + LatexGenerator.get_matrix_code(minor, MatrixTypes.VMATRIX)
            if key == 0:
                text += '-'
            elif key == 1:
                text += '+'
        text += f'={LatexGenerator.normalize_number(result)}'
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
        text += LatexGenerator.get_new_formul_block('A^{-1}=' + LatexGenerator.get_matrix_code(result))
        return text
        