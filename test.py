
import random
"""
res = random.sample(range(1, 50), 7)

ran_list = []
for x in res:
    
    ran_list.append(x)

print(ran_list)
print(ran_list[0])
print(ran_list[-1])

"""
def numCheck(num):
    if num < 0:
        return "negative"
    elif num > 0:
        return "positive"
    else:
        return "zero"
        
print(numCheck(-5))
print(numCheck(0))
print(numCheck(5))

numList = [x for x in range(1,11)]
word = "word"
for i in numList:
    print(i * i)


def guessNumber(x = random.randint(1,50)):
    try:
        guess = int(input("What is your guess?:"))
        if guess < 0:
            raise ValueError("Number entered is a negative number.")
    except ValueError:
        guess = int(input("Please, guess with a positive number value:"))
    
    print(x, guess)
    
    while guess != x:

        if guess > x:
            print("Your guess was wrong and higher.")
        else:
            print("Your guess was wrong and lower.")
        guess = int(input("Guess again:"))
    print("You guessed it right!!")
    
guessNumber()