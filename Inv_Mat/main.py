from Matrix import *
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
print(answer.get_inverse_matrix_with_comment())
print(answer.get_determinant())