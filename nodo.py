# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:31:36 2020
This class object is used to create and store nodes informations,
such as node_number, x coordinate and y coordinate for 2D problems.
This is a simple class, how to use it:
	A = (1, 0.0, 5.0) # Store information about the node_number
	
Call information list:
	print(A.nnodo) # return the node number
	print(A.coordx) # return x coordinate of node A
	print(A.coordy) # return y coordinate of node A
	
All nodes added in yout code will be also stored in a list.
list recall:
	print(nodo.nodelist) # return a list of all nodes added
	
You can also call an integer that count nodes number:
	print(nodo.conta) #return node number

@author: Gaetano Camarda - MSc graduated student at University of Palermo

																	V 1.0
"""

class nodo:
    conta = 0
    nodelist = []
    def __init__(self,nnodo,coordx,coordy):
        self.nnodo = nnodo
        self.coordx = coordx
        self.coordy = coordy
        nodo.conta +=1
        nodo.nodelist.append([self.nnodo,self.coordx,self.coordy])

        


    