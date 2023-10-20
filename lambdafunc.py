def double(x):
    # print(x*2)
    return x*2
    
print(double(5))    

double=lambda x: x*2
print(double(10))

cube=lambda x:x*x*x
print(cube(10))

avg=lambda x,y:(x+y)/2
print(avg(10,10))

# PASSING FUNCTION THROUGH FUNCTION

def appl(fx,value):
    return 10+fx(value) 
print(appl(cube,10))