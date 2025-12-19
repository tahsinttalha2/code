menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price = 0

while True:
    try: 
        order = input("Item: ").title()

        if  order in menu:
            if price > 0:
                price += menu[order]
            else:
                price = menu[order]
            print(f"Total: ${price:.2f}")
    except EOFError:
        break
