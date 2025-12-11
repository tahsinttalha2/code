s = input("camelCase: ")
string = []

a = 0
b = 0
for i in s:
    if i.isupper() == True:
        string.append(s[a:b])
        a = b
    b += 1
string.append(s[a:])

new_string = "_".join(string)

print(new_string.lower())