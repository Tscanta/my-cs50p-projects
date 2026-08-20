import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

before = sys.argv[1]
after = sys.argv[2]

try:
    with open(before) as file:
        reader = csv.DictReader(file)

        with open(after, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["first","last","house"])

            writer.writeheader()

            for row in reader:
                name = row["name"]
                last,first = name.split(", ")
                house = row["house"]

                writer.writerow({
                    "first": first,
                    "last": last,
                    "house": house
                })

except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")
