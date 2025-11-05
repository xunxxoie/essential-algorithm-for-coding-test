finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def is_existing_target_number_binary(target, array):
    start_index = 0
    end_index = len(array) - 1
    mid_index = (end_index - start_index) // 2

    while start_index <= end_index:
        if array[mid_index] == target:
            return True
        elif array[mid_index] > target:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

        mid_index = (end_index + start_index) // 2

    return False

for i in range(1, 17):
    print("i = " + str(i))
    print(is_existing_target_number_binary(i, finding_numbers))
    print()

# 이진 탐색의 시간 복잡도는 O(log n)