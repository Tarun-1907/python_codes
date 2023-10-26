class myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"{self._value}")
    @property
    def value(self):
        return self._value
    
obj=myclass(10)
obj.show()