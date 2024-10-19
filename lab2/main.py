"""
z = 2x1 + 3x2(max)

-3x1 + 2x2 <= 6,
x1 - 4x2 <= 2,
x1 - x2 <= 5,
x1,2 >= 0.
"""
import numpy as np
from scipy.optimize import linprog

z = [2, 3] 

coefficient_1 = [[-3, 2],
                 [1, -4],  
                 [1, -1]]

coefficient_2 = [6, 2, 5] 

x = (0, None)
y = (0, None)

res = linprog(z, A_ub=coefficient_1, b_ub=coefficient_2,  bounds=(x, y), method='simplex', options={"disp": True})  
print(res)

"""
Optimization terminated successfully.
         Current function value: 0.000000    
         Iterations: 5
 message: Optimization terminated successfully.
 success: True
  status: 0
     fun: 0.0
       x: [ 0.000e+00  0.000e+00]
     nit: 5
"""