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
        rtb.RevoluteDH(d=0.45, a=0.15, alpha=np.deg2rad(-90), offset=0, qlim=[np.deg2rad(-170), np.deg2rad(170)]),
        rtb.RevoluteDH(d=0, a=0.83, alpha=np.deg2rad(0), offset=np.deg2rad(-90), qlim=[np.deg2rad(-185), np.deg2rad(65)]),
        rtb.RevoluteDH(d=0, a=0, alpha=np.deg2rad(-90), offset=0, qlim=[np.deg2rad(-137), np.deg2rad(163)]),
        rtb.RevoluteDH(d=0.66, a=0, alpha=np.deg2rad(90), offset=0, qlim=[np.deg2rad(-185), np.deg2rad(185)]),
        rtb.RevoluteDH(d=0, a=0, alpha=np.deg2rad(-90), offset=0, qlim=[np.deg2rad(-120), np.deg2rad(120)]),
        rtb.RevoluteDH(d=0.08, a=0, alpha=np.deg2rad(0), offset=0, qlim=[np.deg2rad(-350), np.deg2rad(350)])
    ],
    name="Kuka KR8 R1620", base=SE3(0, 0, 0)
)
print(robot)


#para modificar ángulos
joint1= np.deg2rad(0)
joint2= np.deg2rad(0) 
joint3= np.deg2rad(0)
joint4= np.deg2rad(0)
joint5= np.deg2rad(0)
joint6= np.deg2rad(0)


q=np.array([joint1, joint2, joint3, joint4, joint5, joint6])
robot.teach(q)