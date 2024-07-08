from collections import deque

def is_palindrome(input_string):
    normalized_string = ''.join(input_string.lower().split())
    
    char_deque = deque(normalized_string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Was it a car or a cat I saw"))
print(is_palindrome("No lemon, no melon"))
print(is_palindrome("Hello World"))