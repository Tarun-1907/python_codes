def say_hello():
    print("Hello")
    print("Good Morning")
def no_rply():
    print("")
def say_h():
    print("Hiiiii")
    print("Nice to meet you.")
def say_bye():
    print("Bye! Have a nice day.")

match input("Want acknowledge or not (Yes or No)? "):
    case "Yes":
       say_hello()
    case "No":
        no_rply()
        
match input("Hello or Bye ? "):
    case "Hello":
        say_h()
    case "Bye":
        say_bye()
    case _:
        print("Invalid Input")