def main():
    name = input("Input: ")
    name = shorten(name)
    print(name)

def shorten(word):
    word = word.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","").replace("O","").replace("A","").replace("E","").replace("I","").replace("O","").replace("U","").replace("O","").strip()
    return word

if __name__ == "__main__":
    main()