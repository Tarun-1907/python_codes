import tkinter as tn 
r=tn.Tk()
lp=tn.Label(r,text="Welcome")
lp.pack(pady=60)
name=input("Enter your name: ")
def hello():
    lp.config(text=f"Hello {name} !! \n Have a nice day :) ")
btn=tn.Button(r,text="Click here",command=hello)
btn.pack(pady=19)
r.mainloop()