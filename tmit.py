import timeit
ms= "x=2";"y=6";"Add=x+y"
ms0= "x=2";"y=6";"Sub=x-y"
ms1= "x=2";"y=6";"Mult=x*y"
ms2= "x=2";"y=6";"Div=x/y"

print(timeit.timeit(ms))
print(timeit.timeit(ms0))
print(timeit.timeit(ms1))
print(timeit.timeit(ms2))