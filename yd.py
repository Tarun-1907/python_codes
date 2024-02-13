def func():
    yield "hello world"    # yield is a keyword in python
# func()
print(next(func()))