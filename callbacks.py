from window import app
from calcs import DeterminantCalc
from latex import LatexGenerator

@app.determinant_callback()
def determine_calc(matrix):
    det = DeterminantCalc.get_det(matrix)
    if len(matrix) == 2:
        return LatexGenerator.get_determinant_code2(matrix, det)
    return LatexGenerator.get_determinant_code3(matrix, DeterminantCalc.get_determinat3(matrix), det)

@app.reverse_callback()
def reverse_calc():
    pass