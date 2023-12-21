from array import *
vals=array('i',[1,2,3,4,5,6,7,8,9,10]) 
newarr=array(vals.typecode, (a**4 for a in vals))
i=0
while i<len(newarr):
    print(newarr[i])
    i+=2
    