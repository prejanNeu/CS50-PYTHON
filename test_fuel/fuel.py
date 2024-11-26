def main():
        try:
            percentage = convert(input())
        except:
            pass

        print(gauge(percentage))

def convert(fraction):
            a,b=fraction.split("/")
            if int(b)==0:
                raise ZeroDivisionError
            if int(a)>int(b):
                raise ValueError
            else:
                return int(round((int(a))*100/(int(b))))

def gauge(percentage):
    percentage=int(round(percentage))
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()