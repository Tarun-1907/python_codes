import time
from itertools import cycle
lights=[('Green',4),
        ('Yellow',1),
        ('Red',4)]

colors=cycle(lights)
while True:
    c,s=next(colors)
    print(c)
    time.sleep(s)