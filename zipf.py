empl=[
     'Rahul',
    'Sumit',
    'Sonit',
    'Ritam'   
]

depr=[
    'HR',
    'Developer',
    'Manager',
    'Data Scientist'
]

age=[
    23,
    35,
    31,
    26
]

cmpy=zip(empl,depr,age)
print(cmpy)

e,d,a=zip(*cmpy)
print(e,d,a)