list=[1,2,3,4,3,2,4,1,2,4,2]
freq=max(set(list), key=list.count) # To find the most frequent number in the list
# max(list) to find the largest number
print(freq)