# A number is a self-divisor if it is evenly divisible by all its digits
# 128 is a self-divisor (128 % 1 == 0, 128 % 2 == 0, 128 % 8 == 0)
# 152 is not a self-divisor (152 % 5 == 2 ≠ 0)
# Any number that has 0 in it is not a self-divisor (division by 0 is undefined)

# First approach: using string conversion
# Precondition: number is a positive int

def is_self_divisor(number):
    number_str = str(number)  # Convert number to a string to loop over digits easily

    for digit_str in number_str:
        digit = int(digit_str)  # Convert each character back to an integer

        # If digit is 0 or number is not divisible by digit, return False
        if digit == 0 or number % digit != 0:
            return False

    return True  # All digits passed the check; it's a self-divisor


# Second approach: without converting to a string
# Uses % 10 to get the last digit and // 10 to remove the last digit
# Precondition: number is a positive int

def is_self_divisor(number):
    target = number  # Store the original number to use in divisibility checks

    while number > 0:
        digit = number % 10  # Get the last digit of the number

        # If digit is 0 or original number is not divisible by digit, return False
        if digit == 0 or target % digit != 0:
            return False

        number //= 10  # Remove the last digit (integer division)

    return True  # All digits passed the check; it's a self-divisor


# Test cases
print(is_self_divisor(128))  # True (1, 2, and 8 divide 128)
print(is_self_divisor(26))   # False (6 does not divide 26)
print(is_self_divisor(152))  # False (5 does not divide 152)
print(is_self_divisor(101))  # False (contains 0)

# Print all self-divisors from 1 to 1000
for number in range(1, 1001):
    if is_self_divisor(number):
        print(number)
