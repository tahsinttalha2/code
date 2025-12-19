import sys
import inflect

names = []

while True:    
    try:
        prompt = input("Name: ")
        names.append(prompt)
    except EOFError:
        print("\nAdieu, adieu, to " + inflect.engine().join(names))
        sys.exit()
