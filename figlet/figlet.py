import pyfiglet
import sys
import random
def main():
    font_list=pyfiglet.Figlet().getFonts()
    if sys.argv[2]  in font_list :
        if (sys.argv[1]=='-f' or sys.argv[1] == '--font'):
            name = input("Input: ")
            result = pyfiglet.figlet_format(name, sys.argv[2])
            print(result)
        else:
            sys.exit("Invalid usage")
    elif len(sys.argv)==1:
        name = input("Input: ")
        result = pyfiglet.figlet_format(name, random.choice(font_list))
        print(result)
    else:
        sys.exit("Invalid usage")
main()