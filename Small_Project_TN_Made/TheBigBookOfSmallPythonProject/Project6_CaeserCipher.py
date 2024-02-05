"""
CAESAR CIPHER, by HaTuongNguyen hatuongnguyen0107@hcmut.edu.vn,
Reference-based on "The big book of small Python projects" - AL SWEIGART
"""

import string as _string
import sys as _sys

try:
    import pyperclip as _pyperclip
except ImportError:
    try:
        from importlib import import_module as _import_module

        pyperclip = _import_module("pyperclip")
    except ImportError:
        print("Module 'pyperclip' is automatically installed, but fail.")
        pass

symbol_list = _string.ascii_lowercase + _string.digits + _string.ascii_uppercase

message = 'Hello world, my name is <NAME>! what is your name?'


def encrypt(string: str, key: int, alphabet: str = symbol_list) -> str:
    result = ''
    length = len(alphabet)
    key %= length

    for symbol in string:
        number = alphabet.find(symbol)

        if number == -1:
            result += symbol
        else:
            number = number + key

            if number >= length:
                number = number - length

            result += alphabet[number]

    return result


def decrypt(string: str, key: int, alphabet: str = symbol_list) -> str:
    return encrypt(string, len(alphabet) - key, alphabet)


__all__ = ('encrypt', 'decrypt')

if __name__ == '__main__':
    if len(_sys.argv) == 3 or len(_sys.argv) == 4:
        message = _sys.argv[1]
        password_key = int(_sys.argv[2])
        if len(_sys.argv) == 4:
            symbol_list = _sys.argv[3]
    else:
        _sys.exit(f'Usage: python CaesarCipher.py <message> <key> <list_of_sample (optional)>')

    encrypted_message = encrypt(message, password_key, symbol_list)
    decrypted_message = decrypt(encrypted_message, password_key, symbol_list)
    print(f"\033[1;93mOriginal Message\033[0m : {message}")
    print(f"\033[1;94mEncrypted Message\033[0m: {encrypted_message}")
    print(f"\033[1;95mDecrypted Message\033[0m: {decrypted_message}")

    try:
        _pyperclip.copy(encrypted_message)
        print("\033[1;92mFull encrypted message copied to clipboard!\033[0m")
    except NameError:
        pass
