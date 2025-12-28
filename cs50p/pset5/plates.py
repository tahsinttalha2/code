def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    length = len(s)
    count = 0

    if length < 2 or length > 6 or s[:2].isalpha() == False or s.isalnum() == False:
        return False

    new_string = s[2:length]
    new_length = len(new_string)

    for i in range(new_length):
        if new_string[i].isdecimal():
            if count == 0 and int(new_string[i]) == 0:
                return False
            else:
                count += 1
        elif new_string[i].isdecimal() == False and count != 0:
            return False
    return True
                   
if __name__ == "__main__":
    main()