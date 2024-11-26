from validators import email

def main ():
    print(check_enail(input("What's your email address? ")))

def check_enail(s):
    if email(s):
        return 'Valid'
    else:
        return 'Invalid'

if __name__ == "__main__" :
    main()
