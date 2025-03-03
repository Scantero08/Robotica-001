import roboticstoolbox as rtb
import spatialmath.base as smb
import spatialmath as sm
import numpy as np
np.set_printoptions(precision=4, suppress=True)

#Crear instancia del Puma560
p560 = rtb.models.DH.Puma560()

#Graficar el robot en su posición inicial (qz)
p560.plot(p560.qz, block=False)

#Definir una matriz homogenea (una traslación y una rotación)
T = sm.SE3.Trans(0.4, 0.1, 0) * sm.SE3(smb.rpy2tr(0,180,0,'deg'))
print(T, "\n")

#Graficar la matriz (sobre el robot)
smb.trplot(T.A, block=True)

#Calcular la cinemática inversa para la matriz de transformación T
q = p560.ikine_a(T) #Defalut: izquierda codo arriba
print(f"Izq, codo arriba:\n {q.q}")
#En grados
print(f"Izq, codo arriba grados:\n {np.rad2deg(q.q)}")
#Mostrar robot en posición calculada
p560.plot(q.q, block=True)

#Calcular inversa con configuración derecha, codo arriba
q = p560.ikine_a(T, config = 'ru')
print(f"Der, codo arriba:\n {q.q}")
#En grados
print(f"Der, codo arriba grados:\n {np.rad2deg(q.q)}")
p560.plot(q.q, block=True)

#Calcular inversa con configuración derecha, codo abajo
q = p560.ikine_a(T, config = 'rd')
print(f"Der, codo abajo:\n {q.q}")
#En grados
print(f"Der, codo abajo grados:\n {np.rad2deg(q.q)}")
p560.plot(q.q, block=True)

#Calcular inversa con configuración izquierda, codo abajo
q = p560.ikine_a(T, config = 'ld')
print(f"Izq, codo abajo:\n {q.q}")
#En grados
print(f"Izq, codo abajo grados:\n {np.rad2deg(q.q)}")
p560.plot(q.q, block=True)
