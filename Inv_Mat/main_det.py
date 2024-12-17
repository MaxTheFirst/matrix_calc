import sys
from Matrix import *
with open("input.txt", "r") as f, open("output.txt", "w") as w:
    sys.stdin = f
    sys.stdout = w
    n, m = list(map(int, input().split()))
    a = []
    for i in range(n):
        b = list(map(Number, input().split()))
        a.append(b)
    answer = Matrix(a)
    if n == 2 and m == 2:
        answer = Matrix2(a)
    elif n == 3 and m == 3:
        answer = Matrix3(a)
    print(answer)
