def sort(A1,A2):
    return sorted(set(A1+A2))

a=[7,6,5,4,7,8,2,1]
b=[4,3,2,5,6,7,4,4]
c=sort(a,b)
print(c)