from calcs import DeterminantCalc
from latex import LatexGenerator

def main():
    array22 = [[1, -2.5], [3, 4]]
    array33 = [[1, -2, 3], [4, 5, 6], [7, 8, 9]]

    print(LatexGenerator.get_determinant_code2(array22, DeterminantCalc.get_det(array22)))
    print(LatexGenerator.get_determinant_code3(array33, DeterminantCalc.get_determinat3(array33), DeterminantCalc.get_det(array33)))

if __name__ == '__main__':
    main()