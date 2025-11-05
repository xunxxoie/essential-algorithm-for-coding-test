finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    array.sort()

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


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)