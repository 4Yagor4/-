r = 0
A = []
B = []
C = []
while r != '':
    r = input()
    v = input()
    if v  == 'Площадь квадрата':
        s1 = int(r) ** 2
        A.append(s1)
    if v == 'Площадь круга':
        s2 = 3.14 * int(r) ** 2
        B.append(s2)
    if v == 'Площадь треугольника':
        s3 = ((int(r) ** 2) * 3 ** 0.5) / 4
        C.append(s3)
print(A,B,C)
