#Frank, Ian and Glen’s Letters
from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

fonts = figlet.getFonts()

#if no font is set the program chooses a random font
if len(sys.argv) == 1:
    font = random.choice(fonts)
    figlet.setFont(font = font)

    #checking if the user has entered a valid font
elif len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

user_input = input("Input: ")

print("Output: ",figlet.renderText(user_input))
