# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:36:09 2020
This class object is used to create and store beam element connectivity,
it is written for simplify variable calls.
ex:
	A = (1, 5, 6) # Add new element beam (element number, nodei, nodej)
	print(A.nelemento) # print the element number
	print(A.nodoi) # print node "i" number
	print(A.nodoj) # print node "j" number
	
The class also create a list that contain all the elements. This list can 
be called using:
	print(elemento.elementlist) # Call a list that contain all element connectivity

You can also call the number of element added:
	print(elemento.conta) # it will return the number of element stored
	
@author: Gaetano Camarda - MSc graduated student at University of Palermo

																	V 1.0
"""

class elemento:
    conta = 0
    elementlist = []
    def __init__(self,nelemento,nodoi,nodoj):
        self.nelemento = nelemento
        self.nodoi = nodoi
        self.nodoj = nodoj
        elemento.conta += 1
        elemento.elementlist.append([self.nelemento,self.nodoi,self.nodoj])
        