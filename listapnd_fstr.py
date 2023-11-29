def apnd(arr):
    n=[]
    a=0
    for i in arr:
        if i!=0:
            n.append(i)
        else:
            a+=1
    n.extend(a * [0])
    return n

a=[1,0,0,2,3,0,4,6,0,4]
print(apnd(a))