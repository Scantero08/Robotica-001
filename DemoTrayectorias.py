import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from spatialmath import *
from spatialmath.base import *
import roboticstoolbox as rtb
np.set_printoptions(suppress=True, precision=4,
                formatter={'float':lambda x: f"{0:8.4g}" if abs(x) < 1e-10 else f"{x:8.4g}"})

font = rtb.rtb_load_jsonfile("data/hershey.json")

#Para una sola letra
letter = font['A']
lift = 0.1 #Altura de la pluma
scale = 0.25 #Escala para tamaño real
via = [] #Lista de puntos para la trayectoria

#Construcción de la trayectoria
for stroke in letter["strokes"]:
    xyz = np.array(stroke) * scale #Convertir stroke en array nx2 y escalar
    xyz = np.pad(xyz, ((0,0),(0,1))) #Agregar columna de ceros z=0
    via.extend(xyz) #Agregar a la lista de puntos
    via.append([xyz[-1,0], xyz[-1,1], lift]) #Agregar punto de levantamiento
    
via = np.array(via) #Convertir a array numpy

xyz_traj =rtb.mstraj(via, qdmax = [0.25, 0.25, 0.25], q0 = [0,0,lift], dt = 0.02, tacc = 0.2,verbose=False).q

#Graficar Resultado
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(xyz_traj[:,0], xyz_traj[:,1], xyz_traj[:,2])
ax.scatter(xyz_traj[0,0], xyz_traj[-1,1], xyz_traj[0,2], color='red', marker='*', label='Inicio') #Inicio
ax.scatter(xyz_traj[-1,0], xyz_traj[-1,1], xyz_traj[-1,2], color='blue', marker='o', label='Final') #Final
#Agregar etiquetas de texto en los puntos
ax.text(xyz_traj[0,0], xyz_traj[0,1], xyz_traj[0,2], "Inicio", color='red')
ax.text(xyz_traj[-1,0], xyz_traj[-1,1], xyz_traj[-1,2], "Final", color='blue')
ax.legend()
#Mostrar plot
plt.show()

#Definir punto xyz donde iniciar el trazo
#Eje Y apunta +Y -> [0,1,0].; Z apunta +Z -> [0,0,-1].
T_pen = SE3.Trans(0.20, 0, 0) * SE3.Trans(xyz_traj) * SE3.OA([0,1,0], [0,0,-1])

puma = rtb.models.DH.Puma560()  
#Calcular cinématica inversa
sol = puma.ikine_LM(T_pen, "lu")
#Mostrar resultado
puma.plot(sol.q, limits=[-0.8,0.8,-0.8,0.8,-0.1,1.0], 
          backend='pyplot', shadow=True, jointaxes=True, block=True)


word = "IMT"
x_offset = 0 #Inicialmente no hay traslación en x
lift = 0.1 #Altura de la pluma
scale2 = 0.125 #Escala 10cm
via = np.empty((0,3)) #Lista de puntos para la trayectoria

for a_letter in word:
    letter = font[a_letter]
    for stroke in letter["strokes"]:
        xyz = np.array(stroke) * scale2 #Aplicar escala al stroke
        xyz[:, 0] += x_offset #Aplicar desplazamiento en x
        xyz = np.pad(xyz, ((0,0),(0,1))) #Agregar columna de ceros z=0
        #Levantar pluma antes de moverse al siguiente trazo
        if via.shape[0] > 0:
            via = np.vstack((via, [via[-1,0], via[-1,1], lift]))
        #Agregar trazo a la lista de puntos
        via = np.vstack((via, xyz[xyz[-1,0], xyz[-1,1], lift]))
        #Levantar pluma antes de moverse al siguiente trazo
        via = np.vstack((via, [xyz[-1,0], xyz[-1,1], lift]))
    #Actualizar el despazamiento en x para la siguiente letra
    x_offset =xyz[-1,0] + 0.05 #Incrementar traslación en x
    
    #Convertir en array numpy
    via2 = np.array(via)
    
    xyz2_traj = rtb.mstraj(via2, qdmax = [0.25, 0.25, 0.25], q0 = [0,0,lift], dt = 0.02, tacc = 0.2, verbose=False).q
    T_pen2 = SE3.Trans(0.20, 0,0)*SE3.Trans(xyz2_traj)*SE3.OA([0,1,0], [0,0,-1])
    
    #Calcular cinemática inversa
    sol2 = puma.ikine_LM(T_pen2, "lu")
    
    #Mostrar resultado
    puma.plot(sol2.q, limits=[-0.8,0.8,-0.8,0.8,-0.1,1.0], 
              backend='pyplot', shadow=True, jointaxes=True, block=True)