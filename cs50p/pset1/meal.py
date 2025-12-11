def main():
    ans = input("What time is it? ").split(":")
    ans = convert(ans)

    if 7 <= ans <= 8:
        print("breakfast time")
    elif 12 <= ans <= 13:
        print("launch time")
    elif 18 <= ans <= 19:
        print("dinner time")

def convert(time):
    t = float(time[0]) + (float(time[1])/60)
    return t

if __name__ == "__main__":
    main()
