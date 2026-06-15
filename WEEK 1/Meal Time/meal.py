#MEAL TIME!

def main():
    user_input = input("What time is it? ") #getting the time from the user
    meal_time = convert(user_input)

    #breakfast, lunch, and dinner timings
    if 7 <= meal_time <= 8:
        print("breakfast time")
    elif 12 <= meal_time <= 13:
        print("lunch time")
    elif 18 <= meal_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")#splits the time
    #converting from string to integers
    hours = int(hours)
    minutes = int(minutes)
    hours += (minutes/60)
    return hours

if __name__ == "__main__":
    main()

