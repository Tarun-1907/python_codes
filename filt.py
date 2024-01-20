def func():
 if num%3 and num%5:
    return True

num=[1,2,3,4,5,6]
filt=filter(func,num)

print(filt)