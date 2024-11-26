import random


def main():
    marks=0
    level=get_level()

    for i in range (10):

        X=generate_integer(level)
        Y=generate_integer(level)
        z=int(input(f"{X} + {Y} = "))

        if z==X+Y:
            marks=marks+1
        else:
            print("EEE")
            for j in range (2):
                z=int(input(f"{X} + {Y} = "))
                if z==X+Y:
                    marks=marks+1

                elif j ==1:
                    print(f"{X} + {Y} = {X+Y}")
                else:
                    print("EEE")
    print (f"Score: {marks}")


def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if 1<=level<=3:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level==1:
        x=random.randint(0,9)
        return x
    elif level ==2:
        x=random.randint(10,99)
        return x
    elif level==3:
        x=random.randint(100,999)
        return x

if __name__ == "__main__":
    main()