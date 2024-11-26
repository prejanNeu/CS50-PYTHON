import sys
import csv
from tabulate import tabulate
try:
    if len(sys.argv)<2:
        print("Too few command-line arguments")
    elif len(sys.argv)>2:
        print("Too many command-line arguments")
    file_name=sys.argv[1]

    with open(sys.argv[1],"r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        data = [row for row in csv_reader]
        print(tabulate(data, header, tablefmt="grid"))



except (FileNotFoundError,NameError):
     if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")
        sys.exit(1)
     else:
        sys.exit("File does not exist")
        sys.exit(1)
