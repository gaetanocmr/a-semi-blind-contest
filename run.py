# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:37:09 2020
This code, solve the problem proposed by portwooddigital:

https://portwooddigital.com/2020/03/01/a-semi-blind-kind-of-contest/

It uses OpenSeesPY for resolution.

@author: Gaetano Camarda - MSc graduated student at University of Palermo

																	V 1.0
																	
"""
import os
clear = lambda: os.system('cls')  # On Windows System
clear()

from openseespy.postprocessing.Get_Rendering import * 
from openseespy.opensees import *
import numpy as np
from nodo import nodo
from elemento import elemento
import LibUnits as lib
from PlotFrame import *
# remove existing model
wipe()

# set modelbuilder
model('basic', '-ndm', 2, '-ndf', 3)

# Coordinate definition --
X1 = 0
X2 = 3048
X3 = X2 + X2

Y1 = 0
Y2 = 3099
Y3 = Y2 + 2793

# Definition Node and Element 

A = nodo(0,X1,Y1)
B = nodo(1,X3,Y1)
C = nodo(2,X3,Y3)
D = nodo(3,X1,Y3)
E = nodo(4,X1,Y2)
F = nodo(5,X3,Y2)
G = nodo(6,X2,Y2)
nnode = nodo.conta
nodematrix = nodo.nodelist

BRB = elemento(0,A.nnodo,G.nnodo)
HSS1 = elemento(1,G.nnodo,C.nnodo)
HSS2 = elemento(2,G.nnodo,B.nnodo)
W1 = elemento(3,A.nnodo,E.nnodo)
W2 = elemento(4,B.nnodo,F.nnodo)
W3 = elemento(5,F.nnodo,C.nnodo)
W4 = elemento(6,D.nnodo,C.nnodo)
W5 = elemento(7,E.nnodo,D.nnodo)
W6 = elemento(8,E.nnodo,G.nnodo)
W7 = elemento(9,G.nnodo,F.nnodo)
nelementi = elemento.conta
elementmatrix = elemento.elementlist

# Definition Nodes OpenSeespy
for i in range(nnode):
    node(nodematrix[i][0],nodematrix[i][1],nodematrix[i][2])

# Define Materials
Elastic = 200e3
EBRB = 300e3

acciaio = 1
acciaio1 = 2
uniaxialMaterial('Elastic',acciaio,Elastic)
uniaxialMaterial('Elastic',acciaio1,EBRB)

fix(A.nnodo,1,1,1)
fix(B.nnodo,1,1,0)
fix(C.nnodo,0,0,0)
fix(D.nnodo,0,0,0)

# Proprietà sezione
W10_A = 10200
W10_Iy = 43140000
W10_Iz = 125700000

W14_A = 10064.5
W14_Iy = 23933307
W14_Iz = 225181201

BRB_A = 3200
HSS1_A = 11225
HSS2_A = 6710

IDTransf = 1
geomTransf('Linear',IDTransf)

# Controventi
element('Truss',BRB.nelemento,BRB.nodoi,BRB.nodoj,BRB_A,acciaio1)
element('Truss',HSS1.nelemento,HSS1.nodoi,HSS1.nodoj,HSS1_A,acciaio)
element('Truss',HSS2.nelemento,HSS2.nodoi,HSS2.nodoj,HSS2_A,acciaio)

# Colonne
element('elasticBeamColumn',W1.nelemento,W1.nodoi,W1.nodoj,W10_A,Elastic,W10_Iz,IDTransf)
element('elasticBeamColumn',W2.nelemento,W2.nodoi,W2.nodoj,W10_A,Elastic,W10_Iy,IDTransf)
element('elasticBeamColumn',W3.nelemento,W3.nodoi,W3.nodoj,W10_A,Elastic,W10_Iy,IDTransf)
element('elasticBeamColumn',W5.nelemento,W5.nodoi,W5.nodoj,W10_A,Elastic,W10_Iz,IDTransf)

# Travi
element('elasticBeamColumn',W4.nelemento,W4.nodoi,W4.nodoj,W14_A,Elastic,W14_Iz,IDTransf,'-release',1)
element('elasticBeamColumn',W6.nelemento,W6.nodoi,W6.nodoj,W14_A,Elastic,W14_Iz,IDTransf,'-release',1)
element('elasticBeamColumn',W7.nelemento,W7.nodoi,W7.nodoj,W14_A,Elastic,W14_Iz,IDTransf)


plot_model()

load1 = 0.33333
load2 = 0.66666
timeSeries('Linear',1)
pattern('Plain', 1, 1)
load(D.nnodo,load2,0,0)
load(E.nnodo,load1,0,0)

system('BandSPD')
constraints('Plain')
numberer('Plain')
test('NormDispIncr', 1.0e-3, 6)
algorithm('Linear')
integrator('LoadControl', 1)
analysis('Static')


# Run Analysis
analyze(1)

# Save a recorder for node displacements before running the analysis
displacement = []
for i in range(nnode):
    displacement.append(nodeDisp(i))   

PlotFrame(nodematrix,elementmatrix,displacement,10000000,'[mm]')

print(displacement[D.nnodo])



