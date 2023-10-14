def deco(fun):
    def wrap():
        print("Welcome",fun.__name__)
        fun()
        print("ok")
    return wrap

@deco
def say_hello():
    print("Hello")

@deco
def say_bye():
    print("Bye")
    
say_hello()
say_bye()