class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showDetails(self):
        print(f"The name of employee : {self.name} and id is {self.id}")


class programmer(employee):                          # This is a child class
    def show(self):                                  # This function is not in the parent class (employee). So it will through error.
        print("The default language is python")
 
e1=employee("Rohan Das",100)        
e1.showDetails()
e2=programmer('Tarun',16)
e2.showDetails()
e2.show()