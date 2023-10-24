class person:
    name="Tarun"
    occupation="HR"
    def info(self):  # Self is the object 
        print(f"{self.name} is a {self.occupation}")
    
a=person()
b=person()
a.name="Tota"
a.occupation="Acnt"
# print(a.name,a.occupation)
a.info()
b.info()  # It gets a defult value