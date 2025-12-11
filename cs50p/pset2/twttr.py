given = input("Input: ")
output = ""

for i in given:
    if i.lower() not in ('a', 'e', 'i', 'o', 'u'):
        output += i
print(output)