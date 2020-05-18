#Read out the Link
#https://machinelearningmastery.com/index-slice-reshape-numpy-arrays-machine-learning-python/

#Array Indexing
    #1D_indexing
    #2D_indexing

#Array_Slicing
    #1D_indexing
    #2D_indexing

#Array_Slicing
from array import *
s=array('d',[1.5,3.2,4.8,5.4,6.5 ])
print(s[0:5])
print(s[0:3])
print(s[0:-2])
print(s[::-1])


#Array conactenation
from array import *
a=array('i',[1,2,3,4,5,6])
b=array('i',[7,8,9,10])
c=array('i')                 #Empty Array
c=a+b
print("Array c :", c)
