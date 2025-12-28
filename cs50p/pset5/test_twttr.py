from twttr import shorten

def main():
    test_vowel_replacement()

def test_vowel_replacement():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("Hi, it's me!") == "H, t's m!"
    assert shorten("CS50E") == "CS50"

if __name__ == "__main__":
    main()
