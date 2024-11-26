import random

number = random.randint(1,100)
while True:
    try:
        level = int(input("level: "))
        if level>0:
            break
    except ValueError:
        pass

while True:
    try:
        guess=int(input("Guess: "))
        if number>guess:
            print("Too small!")
        elif number<guess:
            print("Too large!")
        else:
            print("Just right!")
            break



    except ValueError:
        pass