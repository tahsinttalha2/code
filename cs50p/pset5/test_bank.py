from bank import value

def main():
    test_checker()

def test_checker():
    assert value("10") == 100
    assert value("hello") == 0
    assert value("h") == 20
    assert value("Hi!") == 20

if __name__ == "__main__":
    main()
