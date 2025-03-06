import sympy as sp
from sympy.matrices import rot_axis3

#matriz DH
from spatialmath import *
from spatialmath.base import *
#para graficar
import matplotlib.pyplot as plt
import numpy as np
#para usar el DH
import roboticstoolbox as rtb

#toolbox
robot = rtb.DHRobot(
    [
        rtb.RevoluteDH(d=0.0985, a=0, alpha=np.deg2rad(-90), offset=0, qlim=[np.deg2rad(-175), np.deg2rad(175)]),
        rtb.RevoluteDH(d=0.1405, a=0.408, alpha=np.deg2rad(-180), offset=np.deg2rad(-90), qlim=[np.deg2rad(-175), np.deg2rad(175)]),
        rtb.RevoluteDH(d=0.1215, a=0.376, alpha=np.deg2rad(180), offset=0, qlim=[np.deg2rad(-175), np.deg2rad(175)]),
        rtb.RevoluteDH(d=0.1025, a=0, alpha=np.deg2rad(90), offset=np.deg2rad(-90), qlim=[np.deg2rad(-175), np.deg2rad(175)]),
        rtb.RevoluteDH(d=0.1025, a=0, alpha=np.deg2rad(-90), offset=0, qlim=[np.deg2rad(-175), np.deg2rad(175)]),
        rtb.RevoluteDH(d=0.094, a=0, alpha=0, offset=0, qlim=[np.deg2rad(-175), np.deg2rad(175)])

    ],
    name="Aubo i5", base=SE3(0, 0, 0)
)
#Ponemos el TCP alineado con el brazo
robot.tool = SE3.OA([0, 1, 0], [0,0,1]) #Right, elbow up
robot.configurations_str('ru') #Valores en 0
robot.qz = (0, 0, 0, 0, 0, 0) #Valores en 0

#Verificar que el robot quedo igual en DH y en Toolbox
print(robot)

#Graficamos
robot.plot(q = robot.qz, limits = [-0.8, 0.8, -0.8, 0.8, -0.1, 1], eeframe = True, backend='pyplot', shadow = True, jointaxes = False, block=True)

#Puntos en el espacio x, y, z
#Ojo, debe ser np.array apra poder pasarlo a mstraj
T = np.array([
    [-0.08, 0.08, 0.15],            #A
    [-0.08, 0.08, 0.15 +0.16],      #B
    [-0.08, -0.08, 0.15 + 0.16],    #C
    [-0.08, -0.08, 0.15],           #D
    [0.08, -0.08, 0.15],            #E
    [0.08,- 0.08, 0.15 + 0.16],     #F
    [0.08, 0.08, 0.15 + 0.16],      #G
    [0.08, 0.08, 0.15],             #H
    [-0.08, 0.08, 0.15]             #A
])
via = np.empty((0, 3))
for punto in T:
    xyz = np.array(punto)
     #print(xyz)
    via = np.vstack((via, xyz)) #Agregamos los puntos al array
 
xyz_traj = rtb.mstraj(via, qdmax = (0.5, 0.5, 0.5), dt = 0.02, tacc=0.2).q 
 
fig = plt.figure()
ax= fig.add_subplot(111, projection='3d')
plt.plot(xyz_traj[:,0], xyz_traj[:,1], xyz_traj[:,2])
ax.scatter(xyz_traj[0,0], xyz_traj[0,1], xyz_traj[0,2], color='red', marker = '*') #Inicio
ax.scatter(xyz_traj[-1,0], xyz_traj[-1,1], xyz_traj[-1,2], color='green', marker = 'o') #Final  
plt.show()

T_tool = SE3.Trans(-0.3,0,0) * SE3.Trans(xyz_traj)*SE3.OA([0, -1, 0], [1,0,0]) #Right, elbow up

sol = robot.ikine_LM(T_tool, 'lu')
print(sol.success)
robot.plot(q = sol.q, limits= [-0.3, 0.6, -0.6, 0.6, -0.1, 1], eeframe = True, block = True, backend='pyplot', shadow = True, jointaxes = True)

