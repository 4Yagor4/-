№2 Определить, лежит ли заданная точка внутри или вне треуголь-ника с вершинами в точках (-1, 0), (1, 0), (0, 1).

x = int(input())
y = int(input())
if  y>=0 and y +abs(x) <=1:
    print("Принадлежит")
else:
    print('Не принадлежит')
