import re   # It will import regular expression
conditions="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"# [a-z means all lower case alphabets,
                                                     # + means adding other conditions,
                                                     # \w means searching in the string,
                                                     # 0-9 means all the numbers,
                                                     # ? means one chr or num only 0 or 1 time possible else it will make it false,
                                                     # {2,3} means condition
                                                     # $ means backward search
                                                     # ]
email=input("Enter an email: ")
if re.search(conditions,email):
    print("Valid email")
else:
    print("Wrong email")  
    