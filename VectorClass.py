Point##########################################################
#   CS217:      VectorClass
#   Assignment: Lab 4.py
#   Author:     James Burch
#   Date:       11/17/2016
#   Filename:   .py
#   Purpose:    Python class modeling a Vector in 3 dimentional space
#               -- not all operators that can operate on vectors are
#               implemented in this excersice.
##########################################################

from math import sqrt


class Vector:
    #Constructors
    def __init__(self, x=0.0, y=0.0, z=0.0):

        self.__x=x
        self.__y=y
        self.__z=z

    #Setters and Getters
    def setX(self, newX):
        self.__x = newX
    def getX(self, newX):
        return self.__x

    def setY(self, newY):
        self.__y = newY
    def getY(self, newY):
        return self.__y

    def setZ(self, newZ):
        self.__z = newZ
    def getZ(self, newZ):
        return self.__z

    def mag(self):
        return formatV(sqrt(self.__x**2+self.__y**2+self.__z**2))


    # Special method for converting Vector to a string
    def __str__(self):
        return '['+str(formatV(self.__x)) + ',' + str(formatV(self.__y))+',' + str(formatV(self.__z)) + ']'



    # Special methods for overloading operators

    # Multiplication
    def __mul__(self, RHS):
        if isinstance(RHS, Vector): #Dot product
            return Vector(self.__x * RHS.__x+self.__y*RHS.__y+self.__z*RHS.__z)
        elif isinstance(RHS, (int, float)): #Scaler Product
            return Vector(self.__x * RHS, self.__y * RHS, self.__z * RHS)
        else: #invalid returning self
            return self

    def __rmul__(self, LHS):
        if isinstance(LHS, (int, float)):
            return Vector(LHS * self.__x, LHS * self.__y, LHS * self.__z)
        else: # Invalid Left and side
            return self

        #Addition
    def __add__(self, RHS):
        if isinstance(RHS, Vector): #Vector + Vector
            return Vector(self.__x+RHS.__x,self.__y+RHS.__y,self.__z+RHS.__z)
        elif isinstance(RHS, (int,float)): # Vector + int/float
            return Vector( self.__x + RHS, self.__y + RHS, self.__z + RHS)
        else: # invalid RHS type
            return self

    def __radd__(self, LHS):
        if isinstance(LHS, (int, float)):#int/float + Vector
            return Vector(LHS + self.__x, LHS + self.__y, LHS + self.__z)
        else: # invalid RHS type
            return self

        #Subtraction
    def __sub__(self, RHS): # Vector - vector or float/int
        if isinstance(RHS, Vector): #Vector + Vector
            return Vector(self.__x - RHS.__x,self.__y - RHS.__y,self.__z - RHS.__z)
        elif isinstance(RHS, (int,float)): # Vector + int/float
            return Vector( self.__x - RHS, self.__y - RHS, self.__z - RHS)
        else: # invalid RHS type
            return self

    def __rsub__(self, LHS): #int/float - vector
        if isinstance(LHS, (int, float)):#int/float + Vector
            return Vector(LHS + self.__x, LHS - self.__y, LHS - self.__z)
        else: # invalid RHS type
            return self

    def __neg__(self):# Unary negation operator (e.g., -VecA)
        return Vector(-1*self.__x, -1* self.__y, -1*self.__z)

        # Division
    def __truediv__(self, RHS): # Vector/ int or float
        if isinstance(RHS, (int, float)):
            if RHS != 0:
                return Vector(self.__x / RHS, self.__y / RHS, self.__z / RHS)
        return self #RHS invalid type or zero

    def __xor__(self, RHS): #Vector cross-product -- implements the ('^') operator
        if isinstance(RHS, Vector):
            return Vector(self.__y * RHS.__z - self.__z * RHS.__y,\
                          self.__z * RHS.__x - self.__x * RHS.__z,\
                          self.__x * RHS.__y - self.__y * RHS.__x)
        else: # invalid RHS type
            return self

        #equatlity
    def __eq__(self, RHS): #Vector eqaulity operator
        vectorEqual = bool(self.__x == RHS.__x and self.__y == RHS.__y and self.__z == RHS.__z)
        return vectorEqual



        #greater then
    def __lt__(self, RHS): # VecA < VecB
        return bool(self.mag() < RHS.mag())




def formatV(Vector):
    return ("{:0.3f}".format(Vector))

if __name__ =='__main__':

    VecA = Vector(3,4,5)
    VecB = Vector(1,2,3)
    vecE= (VecA + VecB)
    print(vecE)
    '''
    print(VecA , "=" ,VecA,":",VecA == VecA)
    print(VecA == VecB)
    print("Vector =", VecA)
    print("Vector =", VecB)
    print("Scalar A * B =", VecA * VecB)
    print("Vector A * 2=", VecA * 2)
    print("Vector A * Helen", VecA * "Helen")
    print("Vector A Magnitude = ", VecA.mag())
    print("3 * Vector b = ", 2 * VecB)
    print("Vector A + Vector B", VecA + VecB)
    print("Vector B + Vector A", VecB + VecA, formatV(((VecB + VecA).mag())))
    print("Scalar A - B =", VecA - VecB)
    print("Scalar A - A =", VecA - VecA)
    print( VecA == VecA)
    print(VecB < VecA)
    print(VecA < VecB)
    print(VecA * 2, )
    '''
