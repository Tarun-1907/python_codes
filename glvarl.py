gl_varl=100             # Global variable
def func():
    i=0
    lv=gl_varl              
    for n in range (1000):
        i+=lv*i
    return i
func()