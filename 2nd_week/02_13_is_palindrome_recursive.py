def is_palindrome(string):
    if len(string) == 1 or len(string) == 0:
        return 1
    else:
        n = len(string)
        if string[0] == string[n-1]:
            return is_palindrome(string[1: -1])
        else:
            return 0

print(is_palindrome(input()))