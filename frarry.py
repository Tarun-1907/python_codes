from array import *
vals=array('i',[5,9,8,4,2]) 
print(vals.buffer_info())
vals.reverse()
newarr=array(vals.typecode, (a*a for a in vals))
for e in newarr:
    print(e)
