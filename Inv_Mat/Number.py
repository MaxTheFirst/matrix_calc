from math import gcd
class Number:
    def __init__(self, new_string):
        new_string = str(new_string)
        self.__numerator = 0
        self.__denominator = 1
        if new_string == "":
            return
        recount = ""
        kol_point = 0
        kol_slash = 0
        for symbol in new_string:
            if symbol == '-':
                if len(recount) != 0:
                    raise ValueError("Некорректное значение")
                recount += '-'
                continue
            if symbol == ' ':
                continue
            if (symbol.isdigit() or (symbol == '.' or symbol == '/')) and kol_point + kol_slash <= 1:
                if symbol == '.':
                    kol_point += 1
                elif symbol == '/':
                    kol_slash += 1
                    self.__numerator = int(recount)
                    recount = ""
                elif kol_point == 0:
                    recount += symbol
                else:
                    recount += symbol
                    self.__denominator *= 10
                continue
            raise ValueError("Некорректное значение")
        if kol_slash == 0:
            self.__numerator = int(recount)
        if kol_slash == 1:
            self.__denominator = int(recount)
            if self.__denominator == 0:
                raise ValueError("Некорректное значение")
        g = gcd(self.__numerator, self.__denominator)
        self.__numerator //= g
        self.__denominator //= g
        if self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1
    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        return str(self.__numerator) + "/" + str(self.__denominator)
    def __add__(self, other):
        return Number(str(self.__numerator * other.__denominator + self.__denominator * other.__numerator) + '/' +
                      str(self.__denominator * other.__denominator))
    def __sub__(self, other):
        return Number(str(self.__numerator * other.__denominator - self.__denominator * other.__numerator) + '/' +
                      str(self.__denominator * other.__denominator))
    def __mul__(self, other):
        return Number(str(self.__numerator * other.__numerator) + '/' +
                      str(self.__denominator * other.__denominator))
    def __truediv__(self, other):
        return Number(str(self.__numerator * other.__denominator) + '/' +
                      str(self.__denominator * other.__numerator))
    def __abs__(self):
        return Number(str(abs(self.__numerator)) + '/' + str(abs(self.__denominator)))
    def __float__(self):
        return self.__numerator / self.__denominator
    def __eq__(self, other):
        return self.__numerator == other.__numerator and self.__denominator == other.__denominator
    def __ne__(self, other):
        return self.__numerator != other.__numerator or self.__denominator != other.__denominator
    def __repr__(self):
        return str(self)
    def get_numerator(self):
        return self.__numerator
    def get_denominator(self):
        return self.__denominator