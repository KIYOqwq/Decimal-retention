
from decimal import Decimal
from math import pi as PI

n = int(input("请输入圆的半径："))

def circle_area(n):
    if n>=0:
        s=PI*n*n
        s=Decimal(s).quantize(Decimal('0.00'))
        #该方法不会将末尾的0舍去
        return s
    else:
        return 'You must input an integer or float as radius.'

print(circle_area(n))
