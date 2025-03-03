# Referencia T0
T0 = rotz(0,unit='deg')
trplot(T0, dims=[-1,1,-1,1,-1,1], color ='k') #Dibujar

#Sistema de coordenados rotando (TA)
TA = rotz(90, unit='deg')
trplot(TA, dims=[-1,1,-1,1,-1,1], color ='g') #Dibujar

#Definir el punto P con respecto a T0
P = np.array8([1,1,0])
