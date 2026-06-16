#camelCase to snake_case

def main():
    camelCase = input("camelCase: ")

    result = snake_case(camelCase)

    print("snake_case: ", result)

#converter
def snake_case(firstWord):
    for c in firstWord:
        if c.isupper(): #checking if any letter is uppercase or not
            n = "_"+c.lower() #converting to lowercase and adding an underscore in front
            firstWord = firstWord.replace(c,n) #replacing
    return firstWord

main()

