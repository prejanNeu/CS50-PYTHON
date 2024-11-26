def main():
    greet = input("Greeting: ")
    print(f"${value(greet)}")

def value(greeting):
    greeting=greeting.lower().strip().replace(",", " " )
    all_word = greeting.split()
    first_word=all_word[0]
    if  first_word== "hello":
        return 0
    elif first_word.startswith("h"):
        return 20
    else:
        return 100

if __name__ =="__main__":
    main()