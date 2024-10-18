from  math import  *
s = 0
x = int(input())
for n in range (1, 10):
    s += cos(n * x) / (x**(n-1))
    print(s)
