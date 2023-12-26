b=10000
try:
  n=float(input("Enter the amount to deposit: "))
except ValueError:
  print("Please input a valid amount")
b+=n
print(f"Total balance {b}")
