def greet(fx):
  def mfx():
    print("good morning")
    fx()
    print("Thanks for using this function")
  return mfx
@greet
def hello():
  print("Hello")
hello()