##########################################################
#   CS217:      Lab4
#   Assignment: Lab 4.py
#   Author:     James Burch
#   Date:       11/17/2016
#   Filename:   .py
#   Purpose:    Python class modeling a Vector in 3 dimentional space
#               -- not all operators that can operate on vectors are
#               implemented in this excersice.
##########################################################

from VectorClass import Vector

def main():
    vecA = Vector(1.0, 0.0 , 0.0)
    vecB = Vector(0.0 , 1.0 , 0.0)
    vecC = Vector(0.0 , 0.0 , 1.0)
    print(" Vector A:",vecA,"\n","Vector A:",vecB,"\n","Vector A:",vecC)
    print("Vector A dot Vector B", vecA * vecB)
    print("Vector A cross Vector B", vecA ^ vecB)
    print("Vector A cross Vector B", vecB ^ vecA)
    vecA =(vecA * 3.27)
    print("Vector A * 3.27:",vecA, "Magnitude:" , vecA.mag())
    vecB = (4.5 + vecB)
    print("4.5 + Vector B:", vecB,"Magnitude:" , vecB.mag())
    vecC = (vecC - 1.36)
    print("Vector C - 1.36:", vecC,"Magnitude:" , vecC.mag())
    vecD = (vecA - vecB)
    print("Vector D :", vecD, "Magnitude:" , vecD.mag())
    print("Vector A:", vecA ,"Vestor B", vecB)
    print("Vector E= Vector B + A=", sep='')
    vecE=(vecB + vecC)
    print("Vector E", vecE)
    print("Vector B:", vecB ,"Vector C:", vecC)
    print("Vector D * Vector E:",vecD * vecE)
    print("Vector D",vecD ,"Vector E:", vecE)
    print("Cross product of Vector D x Vector E=", vecD ^ vecE)
    print("Vector D",vecD,"Vector E:", vecE)
    vecE = -vecE
    print("Vector -E =",vecE)
    unitE = (vecE / vecE.mag())
    print("Unit Vector for Vector E  is:", unitE)
    print("Vector A = Vector  B:", vecA == vecB )
    print("Vector D < Vector  E:", vecD < vecE)
    vecA = vecB = vecC = Vector(1.5, 2.5, 3.5)
    print("Vector A = Vector  B = Vector C:", vecA == vecB and vecB == vecC )
main()



'''
C:\Anaconda3\python.exe "E:/school/Python 3/Labs/Lab 4/Lab 4.py"
 Vector A: [1.000,0.000,0.000]
 Vector A: [0.000,1.000,0.000]
 Vector A: [0.000,0.000,1.000]
Vector A dot Vector B [0.000,0.000,0.000]
Vector A cross Vector B [0.000,0.000,1.000]
Vector A cross Vector B [0.000,0.000,-1.000]
Vector A * 3.27: [3.270,0.000,0.000] Magnitude: 3.270
4.5 + Vector B: [4.500,5.500,4.500] Magnitude: 8.411
Vector C - 1.36: [-1.360,-1.360,-0.360] Magnitude: 1.957
Vector D : [-1.230,-5.500,-4.500] Magnitude: 7.212
Vector A: [3.270,0.000,0.000] Vestor B [4.500,5.500,4.500]
Vector E= Vector B + A=
Vector E [3.140,4.140,4.140]
Vector B: [4.500,5.500,4.500] Vector C: [-1.360,-1.360,-0.360]
Vector D * Vector E: [-45.262,0.000,0.000]
Vector D [-1.230,-5.500,-4.500] Vector E: [3.140,4.140,4.140]
Cross product of Vector D x Vector E= [-4.140,-9.038,12.178]
Vector D [-1.230,-5.500,-4.500] Vector E: [3.140,4.140,4.140]
Vector -E = [-3.140,-4.140,-4.140]
Unit Vector for Vector E  is: [-3.140,-4.140,-4.140]
Vector A = Vector  B: False
Vector D < Vector  E: False
Vector A = Vector  B = Vector C: True

Process finished with exit code 0
'''