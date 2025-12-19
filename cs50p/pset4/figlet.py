import sys
import pyfiglet
import random

fonts = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1:
    prompt = input("Input: ")
    print(pyfiglet.figlet_format(prompt, font = random.choice(fonts)))
elif len(sys.argv) <= 3:
    try:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
            prompt = input("Input: ")
            print(pyfiglet.figlet_format(prompt, font = sys.argv[2]))
        else:
            sys.exit("Invalid Usage")
    except IndexError:
        sys.exit("Invalid Usage")