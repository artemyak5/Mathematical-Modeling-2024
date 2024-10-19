"""
z = 2x1 + 3x2(max)

-3x1 + 2x2 <= 6,
x1 - 4x2 <= 2,
x1 - x2 <= 5,
x1,2 >= 0.
"""
import numpy as np
from scipy.optimize import linprog

z = [-2, -3]

coefficient_1 = [
    [-3, 2],
    [1, -4],
    [1, -1]
]

coefficient_2 = [6, 2, 5]

bounds = [(0, None), (0, None)]

res = linprog(
    c=z,
    A_ub=coefficient_1,
    b_ub=coefficient_2,
    bounds=bounds,
    method='highs',
    options={"disp": True}
)

print("Результат оптимізації:")
print("Оптимальне значення цільової функції (максимум):", -res.fun)
print("Оптимальні значення змінних x1 та x2:", res.x)
