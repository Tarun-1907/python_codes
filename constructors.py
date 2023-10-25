class person:
    def __init__(self,n,o):
        print("Hey I am a person") # Always invoked
        self.name=n
        self.occ=o
   # name="Tarun"
   # occ="HR"
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a=person("Tarun","HR")
b=person("Tota","Acnt")
# a.name="Tota"
# a.occ="Acnt"
a.info()
b.info()
# print(a.name)        