from enum import Enum, auto
class fruit(Enum):
    Mango=6
    Banana=auto()
    Apple=4
    Grape=auto()
print(fruit(7).name,fruit(5).name)
print(fruit['Mango'].value)