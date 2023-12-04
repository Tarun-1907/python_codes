from array import *
vals=array('i',[5,9,8,4,2]) 
print(vals.buffer_info())
vals.reverse()
print(vals)
for i in range(5):
    print(vals[i])