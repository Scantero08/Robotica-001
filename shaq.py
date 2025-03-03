import numpy as np
import matplotlib.pyplot as plt
from spatialmath import *
from spatialmath.base import *
from math import pi

# Referencia T0
T0 = rotz(0,unit='deg')
trplot(T0, dims=[-1,1,-1,1,-1,1], color ='k') #Dibujar

#Sistema de coordenados rotando (TA)
TA = rotz(90, unit='deg')
trplot(TA, dims=[-1,1,-1,1,-1,1], color ='g') #Dibujar

#Definir el punto P con respecto a T0
P = np.array([1,1,0])
ax = plt.gca()
ax.scatter (P[0], P[1], P[2], color='r', label='P')

#Configurar plot
plt.gca().view_init(elev=25, azim=44) #Perspectiva

#Mostrar la trama
plt.show()