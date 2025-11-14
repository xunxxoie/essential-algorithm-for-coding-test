input = [4, 6, 2, 9, 1]

# 현재 인덱스 = 1
# 비교해야 할 범위 = 0

# 현재 인덱스 = 2
# 비교해야 할 범위 = 1 -> 0

# 현재 인덱스 = 3
# 비교해야 할 범위 = 2 -> 1 -> 0

# 현재 인덱스 = 4
# 비교해야 할 범위 = 3 -> 2 -> 1 -> 0

# 만약 현재 인덱스가 4번인 상황에서 3번이랑 비교했을 때, 이동할 필요가 없으면 즉시 중단하고 다음 인덱스로 이동

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j] >= array[j-1]:
                break
            array[j - 1], array[j] = array[j], array[j - 1]
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))