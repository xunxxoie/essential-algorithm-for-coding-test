input = "abadabac"

def find_not_repeating_first_character(string):
    repeating_count_array = [0] * 26
    for char in string:
        repeating_count_array[ord(char) - ord('a')] += 1

    for char in string:
        if repeating_count_array[ord(char) - ord('a')] == 1:
            return char

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))