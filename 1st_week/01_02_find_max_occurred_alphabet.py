def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        alphabet_occurrence_array[ord(char) - 97] += 1

    max_occurrence, max_occurrence_index = 0, 0

    for index, occurrence in enumerate(alphabet_occurrence_array):
        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_occurrence_index = index

    return chr(max_occurrence_index + 97)


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

# ord() = 특정 문자를 아스키코드 값으로 바꿔주는 함수
# chr() = 특정 아스키코드 값을 문자로 바꿔주는 함수
# 배열에 enumerate() 메서드를 적용하면, index : value 쌍으로 반환