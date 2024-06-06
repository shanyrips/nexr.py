import re
import string


# Custom Exceptions
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, position):
        self.char = char
        self.position = position

    def __str__(self):
        return f"The username contains an illegal character '{self.char}' at position {self.position}"


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short (minimum is 3 characters)"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long (maximum is 16 characters)"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short (minimum is 8 characters)"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long (maximum is 40 characters)"


# Function to check username and password validity
def check_input(username, password):
    # Check username validity
    if not (3 <= len(username) <= 16):
        # Check if the username is too short
        if len(username) < 3:
            raise UsernameTooShort()
        # Check if the username is too long
        else:
            raise UsernameTooLong()

    # Check for illegal characters in the username
    for i, char in enumerate(username):
        if not re.match(r'[A-Za-z0-9_]', char):
            raise UsernameContainsIllegalCharacter(char, i)

    # Check password validity
    if not (8 <= len(password) <= 40):
        # Check if the password is too short
        if len(password) < 8:
            raise PasswordTooShort()
        # Check if the password is too long
        else:
            raise PasswordTooLong()

    # Check for required characters in the password
    if not any(c.isupper() for c in password):
        raise PasswordMissingUppercase()
    if not any(c.islower() for c in password):
        raise PasswordMissingLowercase()
    if not any(c.isdigit() for c in password):
        raise PasswordMissingDigit()
    if not any(c in string.punctuation for c in password):
        raise PasswordMissingSpecial()

    # If all checks pass, print "OK"
    print("OK")


# Main function to get user input and validate
def main():
    while True:
        try:
            # Get username and password input from the user
            username = input("Enter username: ")
            password = input("Enter password: ")

            # Check if the username and password are valid
            check_input(username, password)

            # If valid, exit the loop
            break
        except Exception as e:
            # Print the exception message if invalid
            print(e)


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
