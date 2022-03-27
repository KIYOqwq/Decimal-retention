#coding=utf-8
from decimal import Decimal
from math import pi as PI

n = int(input("请输入圆的半径"))

def circle_area(n):
    if n>=0:
        s=PI*n*n
        s=round(s,2)
        #这种会将末尾的零舍去，不算是真正意义上的保留两位小数
        return s
    else:
        return 0

print(circle_area(n))
