# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 19:39:27 2021

@author: Claudia Carpintero
"""
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
#Leemos los archivos del fichero
f = open ('/Users/34603/Desktop/ciclistas.texto.txt','r')
dataSet = list()
for linea in f: #Recorremos cada linea del archivo
#mensaje = f.readline() #almacena los valores de la primera fila.
  punto = list(float(i) for i in linea.split())
  dataSet.append(punto)
  #print(punto)
  #print('siguiente')
  #Hasta aquí hemos creado una lista de listas con las variables de cada individuo en cada lista de la lista.

#print(dataSet)
X=np.array(dataSet)
#print(X)
X_embedded = TSNE(n_components=2).fit_transform(X)
X_embedded.shape

fig = plt.figure()
ax1 = fig.add_subplot(111)
 # Establecer título
ax1.set_title('Scatter Plot')
 # Establecer etiquetas de eje X
plt.xlabel('X')
 # Establecer etiqueta del eje Y
plt.ylabel('Y')
 # Dibujar diagrama de dispersión
ax1.scatter(X_embedded[0:9,0],X_embedded[0:9,1],c = 'r',marker = 'o')
ax1.scatter(X_embedded[10:21,0],X_embedded[10:21,1],c = 'b',marker = '*')
 # Establecer iconos
plt.legend('x1')
 # Mostrar dibujo


#plt.scatterplot(X_embedded[:,0], X_embedded[:,1])
#plt.show()