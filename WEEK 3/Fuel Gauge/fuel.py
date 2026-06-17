#FUEL GAUGE

while True:
    try:
        fraction = input("Fraction: ")

        x,y = fraction.split("/")

        x = int(x)
        y = int(y)

        if x < 0 or y < 0 or x > y:
            print("INVALID")
            continue

        factor = x / y
        perc = round((factor) * 100)

        if perc <= 1:
            print("E")

        elif perc >= 99:
            print("F")

        else:
            print(f"{perc}%")

        break

    except (ValueError, ZeroDivisionError):
        continue


