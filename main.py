import random
number = random.randint(1,100)
print("YOU HAVE 3 ATTEMPTS IN TOTAL TO GUESS THE RIGHT NUMBER !!")
print("(Hint - It's b/w 0 - 100)")
print("ALL THE BEST !")
for i in range(3):
    ask = int(input("Guess the no. : "))
    if ask != 69:
        print("You are Wrong")
    else:
        print("You Win")
        break
print(number,"is the correct answer")
