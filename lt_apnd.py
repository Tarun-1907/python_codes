def apnd(arr):
    for i in arr:
        if i==0:
            arr.remove(i)
            arr.append(0)
    return arr
a=[1,0,2,0,4,5,0,6,0,4]
print(apnd(a))