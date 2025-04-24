def is_palindrome(word):
    return word == word[::-1]


def is_abecedarian(word):
    for index in range(len(word) - 1):
        curr_letter = word[index]
        next_letter = word[index + 1]

        if curr_letter > next_letter:
            return False

    return True


if __name__ == '__main__':
    print(is_palindrome('kayak'))
    print(is_palindrome('hello'))

    print(is_abecedarian('accept'))
    print(is_abecedarian('brother'))