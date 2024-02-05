import random
import string
import pyperclip

from colorama import Fore, Style, init

init(autoreset=True)


def generate_password(password_len: int, use_symbols=False, use_ambiguous=False) -> str:
    """
  Generate random string of password of preference per user's request

  Parameter:
  ----------
  - **password_len** (integer): The desired length of the password.

  - **use_symbols** (boolean, optional): Whether to include symbols like (@ # $ %) in the password (default is False).

  - **use_ambiguous** (boolean, optional): Whether to include ambiguous characters like { } [ ] ( ) / \ ' " ` ~ , ; : . < > in the password (default is False).

  Returns:
  ----------
  - **String**: The randomly generated password string.

  Usage:
  ----------
  * Call this function to generate a password according to the specified parameters.

  Example:
  ----------
  password = generate_password(12, use_symbols=True, use_ambiguous=True)

  print("Generated Password: ", password)
  """
    
    # Ensure that the password length is at least 4
    try:
        if password_len < 4:
            raise ValueError
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "Password length must be at least 4!!!😾")
        raise ValueError
    
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    print(lowercase_letters)
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = "@#$%"
    ambiguous_chars = "{}[]()/\\'\"`~,;:.<>"
    
    character_sets = [lowercase_letters, uppercase_letters, digits]
    
    if use_symbols:
        character_sets.append(symbols)
    if use_ambiguous:
        character_sets.append(ambiguous_chars)
    
    # Initialize password with one character from each set
    password = [random.choice(char_set) for char_set in character_sets]  # Pick 3 to 5 characters in character sets
    remaining_length = password_len - len(password)
    
    # Generate the rest of the password randomly
    if remaining_length > 0:
        random_chars = [random.choice("".join(character_sets)) for _ in range(remaining_length)]
        password.extend(random_chars)
    
    # Shuffle the password for randomness
    random.shuffle(password)
    print(password)
    return "".join(password)


### Test code
while True:
    try:
        # password_length = int(input("Your desired password length: "))
        # include_symbols = input("Include symbols like (@ # $ %)? (yes/no): ").lower() == "yes"
        # include_ambiguous = input("Include ambiguous characters like { } [ ] ( ) / ' \" ` ~ , ; : . < >? (yes/no): ").lower() == "yes"
        
        password_length = 4
        include_symbols = True
        include_ambiguous = True
        
        generated_password = generate_password(password_length, include_symbols, include_ambiguous)
        
        print(f"{Style.BRIGHT + Fore.BLUE}Generated password: {Fore.GREEN}{generated_password}")
        pyperclip.copy(generated_password)  # Auto copy the password
        print("Your password has been copied to the clipboard.")
    
    except ValueError:
        print(f"{Fore.RED + Style.BRIGHT}{ValueError}")
    
    if input("Do you want to generate another password? (yes/no): ").lower().startswith('n'):
        break
