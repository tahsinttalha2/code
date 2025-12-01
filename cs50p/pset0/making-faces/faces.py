string = input()

if string.find(":)") != -1 and string.find(":(") != -1:
    string = string.replace(":)", "\N{slightly smiling face}").replace(":(", "\N{slightly frowning face}")
elif string.find(":)") != -1 :
    string = string.replace(":)", "\N{slightly smiling face}")
elif string.find(":(") != -1:
    string = string.replace(":(", "\N{slightly frowning face}")

print(string)