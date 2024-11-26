import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count=0
    list =s.lower().split(' ')
    for word in list:
        if re.search(r"^ *um *[?.,]* *$",word):
            count+=1
    return count


if __name__ == "__main__":
    main()