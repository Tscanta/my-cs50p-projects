import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a python file")

try:
    with open(filename) as file:
        count=0
        for line in file:
            if not line.strip():
                continue
except FileNotFoundError:
    sys.exit("File does not exist")

