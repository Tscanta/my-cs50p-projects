# Counting the number of lines
import sys

if len(sys.argv) > 2: #python lines.py hello.py goodbye.py
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2: #python lines.py
    sys.exit("Too few command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"): #python lines.py invalid_extension.txt
    sys.exit("Not a python file")

try:
    with open(filename) as file:
        count=0

        for line in file:
            newline = line.strip()

            if not newline: #skipping all the blank lines
                continue

            if newline.startswith("#"):
                continue

            count += 1
        print(count)

except FileNotFoundError: #python lines.py non_existent_file.py
    sys.exit("File does not exist")

