grocery_list = {}

while True:
    try:
        item = input("")
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:
        break

grocery_list = dict(sorted(grocery_list.items()))
for item in grocery_list:
    print(f"{grocery_list[item]} {item.upper()}")