#python array Documentation
#https://docs.python.org/3.1/library/array.html

#See these videos
#https://www.youtube.com/watch?v=6a39OjkCN5I
#https://www.youtube.com/watch?v=phRshQSU-xAar

#import array as ar
#from array import *
#h=ar.array('i',[1,6,5,8,9])
#print(h)

from array import *

h=array('i',[1,6,5,8,9])
#print(h.buffer_info())
#print(h.typecode)
#h.reverse()
#print(h)

#append    #Add one value at the end
#h.append(12)
#extend     #Add more than one value at the end by using SQUARE brackets
#h.extend([16,17,18])
#insert     #Add one value at specific vale at particular position.
#h.insert(2,55)

#Remove the variables from an array
h.pop()                       #Remove the last variable from the array
#print(h)

h.pop(2)                     #Remove the 2nd element from the array Using Indexing
#print(h)

h.remove(1)                      #Remove the element which we want to remove
print(h)


#For loop for array
#for i in range(len(h)):              #Using len function
#    print(h[i])

#for e in h:      #We can directly acess array variables from h array
 #   print(e)

#newarr= array(h.typecode, (a for a in h))         # copy array h into newarr
#for a in newarr:
#    print(a)