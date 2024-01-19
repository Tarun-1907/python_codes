from collections import Counter
num=Counter(h=1,
            a=-1,
            e=1,
            l=2,
            o=1)

for n in num.elements():       # elements() method is provided by the Counter class
    print(n,num[n])
