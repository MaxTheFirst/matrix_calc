class Number:
    def __init__(self, new_string):
        self.numerator = 0
        self.denominator = 1
        recount = ""
        kol_point = 0
        kol_slash = 0
        for symbol in new_string:
            if symbol.isdigit() or ((symbol == '.' or symbol == '/') and kol_point + kol_slash == 0):
                if (symbol == '.'):
                    print(5)
                continue
            raise ValueError("Некорректное значение")



