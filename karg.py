from operator import mul
def func(*i):
    mn=mul(*i)/sum(i)
    print(mn)
    
func(6,4)