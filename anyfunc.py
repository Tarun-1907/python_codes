work=[
    { 'work remain':4},
    { 'work remain':1},
    { 'work remain':0},
    { 'work remain':2},
    { 'work remain':8},
    { 'work remain':0},
]

if any({i['work remain'] for i in work}):
    {
        print('All work is not done.')
    }
else:
    {
        print('All work is done.')
    }
    
    