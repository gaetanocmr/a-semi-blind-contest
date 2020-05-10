# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:22:49 2020
This function use matplotlib for plot the node displacement of a 2D frame.
It requires at least 2 inputs: nodematrix and elementmatrix. (it is possible to
create this ones using nodo.py and elemento.py).

Optional inputs are:
	- displacement matrix: [x_displacement, y_displacement...]
	- scale factor
	- lenght unit (showed in the plot title)
	
@author: Gaetano Camarda - MSc graduated student at University of Palermo

																	V 1.0
																	
"""
import matplotlib.pyplot as plt
def PlotFrame(nodematrix,elementmatrix,displacement = None,scale = 1,unit ='[mm]'):
    if displacement is None:
        unit = None
        plt.figure()
        for i in range(len(elementmatrix)):
            nodoi = elementmatrix[i][1]
            nodoj = elementmatrix[i][2]
            xx = (nodematrix[nodoi][1],nodematrix[nodoj][1])
            yy = (nodematrix[nodoi][2],nodematrix[nodoj][2])
            plt.plot(xx, yy,'-b');
        plt.savefig('displacement.eps', format='eps')
    elif displacement is not None:
        nodematrix_update = []
        plt.figure()
        for i in range(len(elementmatrix)):
            nodoi = elementmatrix[i][1]
            nodoj = elementmatrix[i][2]
            xx = (nodematrix[nodoi][1],nodematrix[nodoj][1])
            yy = (nodematrix[nodoi][2],nodematrix[nodoj][2])
            plt.plot(xx, yy,'-b');
        txt = ('Frame nodes displacements ' + unit + ' (Scale factor: ' + str(scale) + ')')
        plt.title(txt)
        for i in range(len(nodematrix)):
            nodematrix_update.append([nodematrix[i][0],nodematrix[i][1]+displacement[i][0]*scale,nodematrix[i][2]+displacement[i][1]*scale])
        for i in range(len(elementmatrix)):
            nodoi = elementmatrix[i][1]
            nodoj = elementmatrix[i][2]
            xx = (nodematrix_update[nodoi][1],nodematrix_update[nodoj][1])
            yy = (nodematrix_update[nodoi][2],nodematrix_update[nodoj][2])
            plt.plot(xx, yy,'-r');
        plt.savefig('nodes_displacement.eps', format='eps')
        
        
