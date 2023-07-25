def main():
    mass = int (input("M: "))
    print("E : " , einstein(mass))

def einstein(n):
    return n*pow(300000000,2)

main()