a=input("Enter the number: ")
print(f"multipliction of {a} is: ")

try:
  for i in range (1,11):
    print(f"{int(a)} x {i} ={int(a)*i}")
# except Exception as e:
#    print(e)    
 
# except:
#    print("Invalid input")    
    
except ValueError:
    print("Value is invalid")
    
except SystemError:    
    print("Servererror")
    
print("Some lines of codes")