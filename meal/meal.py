def main():
    time=input("What time is it? ")
    # I am supposing the 00:00 0 minate and add the minuate the variable
    z=convert(time)
    if (7.0<=z<=8.0):
        print("breakfast time")
    elif(12.0<=z<=13.0):
        print("lunch time")
    elif (18.0<=z<=19.0):
        print("dinner time")
def convert(time):
    x,y=time.split(":")
    z=int(x)+int(y)/60
    return z;

if __name__ == "__main__":
    main()