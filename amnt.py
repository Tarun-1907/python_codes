price=int(input("Enter the amount here: "))
good=True
if good:
    print("You need to put down 10%")   
    down_payment=0.1*price
else:
    print("You need to put down 20%")  
    down_payment=0.2*price
print(f"Down payment: ${down_payment}")
total_payment=price+down_payment    
print(f"Total payment: ${total_payment}")