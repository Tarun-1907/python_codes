number=10
guess_num=0
guess_limit=5
while guess_num<guess_limit:
    guess=int(input('Guess: '))
    guess_num+=1
    if guess==number:
        print("Welcome")
        break
    else:
        print("Try again")
        