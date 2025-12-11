due = 50

print(f"Amount Due: {due}")
while True:
    insert = int(input("Insert Coin: "))
    if insert in (25, 10, 5):
        due -= insert

    if due <= 0:
        print(f"Change Owed: {abs(due)}")
        break
    print(f'Amount Due: {due}')