#THE ANSWER TO THE GREAT QUESTION OF LIFE

users_answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
users_answer = users_answer.lower().strip()

if(users_answer == "forty two" or users_answer == "42" or users_answer == "forty-two"):
    print("Yes")
else:
    print("No")

