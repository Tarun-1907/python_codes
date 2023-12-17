def make_even(num):
    if num%2==1:
        return num+1
    else:
        return num
x=[453,332,453,232,876,789,987,164,843,544]
y=map(make_even,x)                      # Using the map function
print(y)