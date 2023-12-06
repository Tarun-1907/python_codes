avai=1000
x=int(input('How many candies you want ?'))
i=1
while i<=x:
    if i>avai:
        print('out of stock')
        break
    print('candy')
    i+=1
print(f"Only {1000-x}  candies is in the stock." )
print('bye')