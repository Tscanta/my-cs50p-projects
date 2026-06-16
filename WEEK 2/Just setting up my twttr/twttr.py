#OMITTING VOWELS

def main():
    user_input = input("Input: ")

    result = omit_vowels(user_input)

    print("Output: ",result)

def omit_vowels(word):
    for i in word:
        if i in "AEIOUaeiou": #checks if the input contains any of these letters (vowels)
            word = word.replace(i,'') 
    return word

main()



