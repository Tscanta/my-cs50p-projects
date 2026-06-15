#TIP CALCULATOR

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


#Removing the dollar sign and converting 'd' to a float variable
def dollars_to_float(d):
    d = d.replace('$',' ').strip()
    return float(d)


#Removing the percentage sign and converting 'p' to a float variable
def percent_to_float(p):
    p = p.replace('%',' ').strip()
    return float(p)/100

main()
