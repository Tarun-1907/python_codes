i=int(input("Enter a number: "))
for j in range(2,i):
    if i%j==0:
        print('Not prime')
else:
     print('prime')  