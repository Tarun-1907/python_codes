import threading as td
def func():
    print("Hello")
t=td.Timer(6.0,func)
print("Start")
t.start()
print("Done")
