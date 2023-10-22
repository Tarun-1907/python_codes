# There is no public private and protected in python

# public can be accesed by outside
# private cannot accessed by outside (prefix its name using __)
# protected can be accessed in the class or can be accessed by the child class (add an underscore in the prefix of the function)

class employee:
    def __init__(self):
        self.__name="Harry"

a=employee()
# print(a.__name)   # Cannot be accessed directly

# Name Mangling
print(a._employee__name)   # Can be accessed indirectly
# a.emp1=10
print(a.__dir__())    # All the methods you can run in a, it will show you it 