import sympy as sp
from sympy.matrices import rot_axis3
#Para poder graficar
import matplotlib.pyplot as plt
import numpy as np
#Para generar la matriz DH
from spatialmath import *
from spatialmath.base import *

#Definir los simbolos
theta, d, a, alpha = sp.symbols('theta, d, a, alpha')

#Matriz RzTzTxRx
TDH = trotz(theta) @ transl(0,0,d) @ transl(a,0,0) @ trotx(alpha)
sp.pprint(TDH)
print(type(TDH))


#Declarandola explicitamente
T = sp.Matrix([
    [sp.cos(theta), -sp.sin(theta)*sp.cos(alpha), sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
    [sp.sin(theta), sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],
    [0, sp.sin(alpha), sp.cos(alpha), d],
    [0, 0, 0, 1]
])
sp.pprint(T)
print(type(T))

