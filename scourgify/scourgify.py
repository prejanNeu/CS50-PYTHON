import sys
i=0
try:

    if len(sys.argv)<3:
        print("Too few command-line arguments")
    elif len(sys.argv)>3:
        print("Too many command-line arguments")
    with open(sys.argv[1],"r") as before_file:
        with open(sys.argv[2],"w") as after_file:
            after_file.write("first,last,house\n")
            for line in before_file:
                if '"' in line:
                    new_line=line.replace('"','')
                    first,second,third=new_line.strip().split(',')
                    after_file.write(f"{second.strip()},{first.strip()},{third.strip()}\n")


except FileNotFoundError:
    print("Could not read invalid_file.csv")
    sys.exit(1)