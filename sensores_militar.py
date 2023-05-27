# -*- coding: utf-8 -*-
"""
Created on Fri May 26 20:15:57 2023

@author: Daniela
"""

import sys
import os
import numpy as np
from PyQt5 import QtCore, QtGui, Qt, QtWidgets, uic
import matplotlib
import matplotlib.pyplot as plt
import math
import datetime
matplotlib.use('Qt5Agg')

x= np.arange(11.0 ,31.0, 0.1)
function_temperatura =  [math.sin(xi) for xi in x]
function_sonido =  [math.cos(xi) for xi in x]
function_vibracion =  [math.sin(xi*3.0) for xi in x]
function_movimiento =  [math.cos(xi*2.0) for xi in x]

now= datetime.datetime.now()


with open("./datos_sensores_militar.txt", "w") as file:
    for i in range(len(x)):
        file.write(str(now) + " " + str(round(x[i],2)) + " " + str(function_temperatura[i]) + " " + str(function_sonido[i]) + " " + str(function_vibracion[i]) + " " + str(function_movimiento[i]) + "\n")




class sensores_militar(QtWidgets.QMainWindow):
 def __init__(self):
     super (sensores_militar, self).__init__()
     uic.loadUi('sensores.ui', self)
     self.Temperatura.clicked.connect(self.a)
     self.Sonido.clicked.connect(self.b)
     self.Movimiento.clicked.connect(self.c)
     self.Vibraciones.clicked.connect(self.d)
     self.Tabla.clicked.connect(self.datos)
     #self.datos()
   
     
 def datos(self):   
   data = []
   with open("./datos_sensores_militar.txt", "r") as file:
       for line in file:
           line_data = line.strip().split()
           data.append(line_data)
           
   self.tabla_sensores.setColumnCount(len(data[0]))
   self.tabla_sensores.setRowCount(len(data))
   self.tabla_sensores.setHorizontalHeaderLabels(["fecha","hora","tiempo","Temperatura","sonido","vibraciones","movimiento"])
   
   
   
   for i , row in enumerate(data):
       for j, item in enumerate(row):
           self.tabla_sensores.setItem(i, j, QtWidgets.QTableWidgetItem(item))
   


 def a(self):
     
    plt.plot(function_temperatura, color='orangered',linestyle='--',marker= 'o' ,markersize=5 , markeredgecolor='blue',markerfacecolor='red')
    plt.ylabel('Temperatura (C)')
    plt.xlabel('sample')
    plt.show()
    
    
    
 def b(self):
    plt.plot(function_sonido,color='orangered',linestyle='-',marker= 'o' ,markersize=5 , markeredgecolor='blue',markerfacecolor='red')
    plt.ylabel('frecuencia(hz)')
    plt.xlabel('sample')
    plt.show()
    
 def c(self):
    plt.plot(function_vibracion,color='orangered',linestyle='-',marker= 'o' ,markersize=5 , markeredgecolor='blue',markerfacecolor='red')
    plt.ylabel('metros cubicos(hz)')
    plt.xlabel('sample')
    plt.show()
    
 def d(self):
    plt.plot(function_movimiento,color='orangered',linestyle='-',marker= 'o' ,markersize=5 , markeredgecolor='blue',markerfacecolor='red')
    plt.ylabel('metros(m)')
    plt.xlabel('sample')
    plt.show()

def main():
    import sys
    print('inicia')
    app=QtWidgets.QApplication(sys.argv)
    ventana=sensores_militar()
    ventana.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()    

