while True:
    fuel = input("fuel: ")
    
    try:
        x, y = fuel.split("/")
        
        x = int(x)
        y = int(y)

        if x <= y: 
            per = (x / y) * 100
            
            if per <= 1:
                print("E")
            elif per >= 99:
                print("F")
            else:
                print(f"{round(per)}%")  
        break

    except ValueError or ZeroDivisionError:
        pass