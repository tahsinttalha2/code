from datetime import datetime

while True: 
    date = input("Date: ")

    try:
        date = datetime.strptime(date, "%m/%d/%Y").strftime("%Y-%m-%d")
        print(date)
        break

    except ValueError:
        try:
            date = date = datetime.strptime(date, "%B %d, %Y").strftime("%Y-%m-%d")
            print(date)
            break
        except:
            pass


