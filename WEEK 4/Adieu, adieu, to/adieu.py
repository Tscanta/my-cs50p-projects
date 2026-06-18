#Adieu, adieu, to
import inflect
p = inflect.engine()

names = [] #an empty list that stores all entered names

while True: #loop
    try:
        name = input("Name: ")
        names.append(name) #adding our names to the list
    except EOFError: #breaks when ctrl+D
        print()
        break

joined_names = p.join(names) #inflect function that joins the names together
print(f"Adieu, adieu, to {joined_names}")

