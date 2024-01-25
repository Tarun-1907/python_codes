from collections import namedtuple

n=namedtuple('Name',['Sumit','Rahul','Sonit','Pravin'])
w=n('Manager','HR','Developer','Intern')
print("Rahul is a",w.Rahul)