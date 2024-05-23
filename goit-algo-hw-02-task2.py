from collections import deque

def is_palindrome(input_string):
    # Create a deque and add all characters of the input string
    char_deque = deque(input_string)

    # Compare characters from both ends of the deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Test
string = "ABCBA"
#string = "ABCbA"


if is_palindrome(string):
    print(f"String: {string} is a palindrome")
else:
    print(f"String: {string} is not a palindrome")
    

