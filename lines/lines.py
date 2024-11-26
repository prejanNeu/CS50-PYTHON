import sys
try:
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    file_name=sys.argv[1]
    count=0
    with open(sys.argv[1],"r") as file :
            for line in file :
                new_line=line.strip()
                if new_line.startswith("#") or len(new_line)==0:
                    count+=0
                else:
                    count+=1
    print(count)
except FileNotFoundError:
     if not file_name.endswith(".py"):
        sys.exit("Not a Python file")
     else:
        sys.exit("File does not exist")