def is_number_exist(number, array):
    for value in array:
        if value == number:
            return True
    return False

result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))

# 최악의 경우에서의 시간복잡도 = 빅오(Big-O)표기법
# 최선의 경우에서의 시간복잡도 = 빅 오메가(Big-Ω) 표기법

# 최선의 경우는 알고리즘에 데이터가 처리하기 쉽게 들어오는 경우를 말한다.
# 하지만, 현실 세계에서는 이러한 경우는 많지 않으므로, 보통 빅오 표기법을 채택한다.