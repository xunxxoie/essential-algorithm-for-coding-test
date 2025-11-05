input = "abcba"

def is_palindrome(string):
    n = len(string)
    for i in range(n // 2):
        if string[i] != string[n- 1 - i]:
            return False
    return True


print(is_palindrome(input))