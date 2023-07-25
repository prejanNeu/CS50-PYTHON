def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i=2
    if 2<=len(s)<=6 and s.isalnum():
        if s.isalpha():
            return True
        for i in range(len(s)):
            if s[i].isdigit():
                break
        part1=s[:i]
        part2=s[i:]
        if part2[0]!= '0' and part2.isdigit():
            return True
        else:
            return False


main()