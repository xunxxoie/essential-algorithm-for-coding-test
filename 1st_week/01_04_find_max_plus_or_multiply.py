def find_max_plus_or_multiply(array):
    sum = 0
    for value in array:
        if sum == 0 or value == 1 or value == 0:
            sum += value
        else:
            sum *= value
    return sum


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))

# 보통 곱셈이 숫자를 커지게 하는데 효과적이지만, 엣지케이스가 있다.
# 0을 곱하면 총합이 0이 되므로 더하는게 낫다.
# 1을 곱하면 총합이 그대로이므로 더하는게 낫다.
# 따라서, 0과 1을 만나면 곱하지 않고 더하면 된다.

# 만약, 초기값이 0인 상태에서 그 다음 숫자가 3이면 곱하지 말고 더해야 한다.
# 즉 합이 0인 경우에 대한 엣지케이스 처리도 추가해야 한다.