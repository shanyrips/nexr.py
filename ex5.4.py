def check_id_valid(id_number):
    """
    Check if the given ID number is valid according to the described algorithm.

    Args:
    - id_number (int): The ID number to be checked.

    Returns:
    - bool: True if the ID number is valid, False otherwise.
    """
    # Convert ID number to string for easy manipulation
    id_str = str(id_number).zfill(9)  # Ensure it's 9 digits by padding with zeros if necessary
    total = 0
    for i, digit in enumerate(id_str):
        num = int(digit)
        if i % 2 == 0:  # Odd index (0-based)
            total += num
        else:  # Even index (0-based)
            double_num = num * 2
            if double_num > 9:
                double_num = (double_num // 10) + (double_num % 10)
            total += double_num
    return total % 10 == 0


class IDIterator:
    """
    Iterator class for generating valid ID numbers.
    """

    def __init__(self, id_):
        self.id_ = id_

    def __iter__(self):
        return self

    def __next__(self):
        """
        Return the next valid ID number in the range from the current ID to 999999999.
        """
        self.id_ += 1  # Increment the ID to check the next one
        while self.id_ <= 999999999:
            if check_id_valid(self.id_):
                return self.id_
            self.id_ += 1
        raise StopIteration  # Stop the iteration if the limit is reached


def id_generator(id_):
    """
    Generator function that yields valid ID numbers starting from the given ID.

    Args:
    - id_ (int): The starting ID number.

    Yields:
    - int: The next valid ID number.
    """
    id_ += 1  # Increment the ID to check the next one
    while id_ <= 999999999:
        if check_id_valid(id_):
            yield id_
        id_ += 1


if __name__ == "__main__":
    # user input
    user_id = int(input("Enter ID: "))
    method = input("Generator or Iterator? (gen/it)? ")
    print(check_id_valid(123456780))
    # checking according to chosen method
    if method == "it":
        id_iter = IDIterator(user_id)
        for _ in range(10):
            print(next(id_iter))
    elif method == "gen":
        id_gen = id_generator(user_id)
        for _ in range(10):
            print(next(id_gen))
    else:
        print("Invalid method. Please choose 'gen' or 'it'.")

