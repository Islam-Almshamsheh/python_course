
import string, random

# print(string.digits) => 0123456789
# print(string.ascii_letters) => abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_lowercase) => abcdefghijklmnopqrstuvwxyz
# print(string.ascii_uppercase) => ABCDEFGHIJKLMNOPQRSTUVWXYZ

def make_serial(count):
    """
    Generates a random series of characters of the given length.
    Parameters:
        count (int): The length of the desired random series.
    1. including all letters in both cases as well as letters in all_chars
    2. selecting a random index from all_chars by random_number to get a random character
    3. making out the random serie by joining out the random characters 
    """
    all_chars = string.ascii_letters + string.digits
    # print(all_chars) => abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

    char_count = len(all_chars)
    # print(char_count) => 62
    serial_list = []

    while count > 0:
        random_number = random.randint(0, char_count-1)

        random_char = all_chars[random_number]

        serial_list.append(random_char)

        count -= 1

    print("".join(serial_list))
    
try:
    serial_length = int(input("Please Enter The Desired Length For Your Random Series of Characters: ").strip())

    if serial_length <= 0:
        print("The length should be greater than 0.")
    else:
        print(f"Generated Random Series: {make_serial(serial_length)}")

except ValueError:

    print("Invalid input! You should enter a valid number.")


# Explanation of why we subtract 1 from char_count:
# Python lists and strings are zero-indexed, meaning that the first element is at index 0 and the last element is at index char_count-1.
# For example, in the string "1234":
# test = "1234"
# print(test[0]) => 1   (index 0 corresponds to the first element)
# print(test[1]) => 2   (index 1 corresponds to the second element)
# print(test[2]) => 3   (index 2 corresponds to the third element)
# print(test[3]) => 4   (index 3 corresponds to the fourth element)
# print(test[4]) => IndexError (because index 4 is out of bounds)
# Therefore, when generating a random index using random.randint, we must use char_count-1 as the upper bound 
# to ensure we don’t exceed the valid index range of all_chars(0, 61) not 62.
(help(make_serial))