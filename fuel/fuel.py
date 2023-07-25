def main():
    x=int(round(get_input()))
    if x<=1:
        print("E")
    elif x>=99:
        print("F")
    else:
        print(f"{x}%")
def get_input():
    while True:
        try:
            fraction=input("Fraction: ")
            a,b=fraction.split("/")
            if int(a)>int(b):
                continue
            else:
                return float((int(a)*100/int(b)))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()