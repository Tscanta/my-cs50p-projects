#Its "hello" not "hey"!

#gets the greeting from the user
greeting = input("Greeting: ")

#converts to lowercase and removes all the whitespaces
greeting = greeting.lower().strip()

#if and else
if(greeting.startswith("hello")):
    print("$0", end="")

elif(greeting.startswith("h")):
    print("$20", end="")

else:
    print("$100", end="")

