operation = input().split(" ")

a = float(operation[0])
b = float(operation[2])



match operation[1]:
    case '+':
        print(f"{a + b}")
    case '-':
        print(f"{a - b}")
    case '*':
        print(f"{a * b}")
    case '/':
        print(f"{a / b}")