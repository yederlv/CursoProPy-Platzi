def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome
    """
    string = string.replace(" ","").lower()     # Ana <> ana
    return string == string[::-1]      


def run():
    print(is_palindrome(2022))


if __name__ == "__main__":
    run()

    