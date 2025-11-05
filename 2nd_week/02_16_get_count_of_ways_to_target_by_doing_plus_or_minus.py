numbers = [1, 1, 1, 1, 1]
target_number = 3

result = []
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    get_all_ways_by_doing_plus_or_minus(array, 0, 0)

    count = 0
    for value in result:
        if value == target:
            count += 1

    return count

def get_all_ways_by_doing_plus_or_minus(array, index, value):
    if index == len(array):
        result.append(value)
        return

    get_all_ways_by_doing_plus_or_minus(array, index + 1, value + array[index])
    get_all_ways_by_doing_plus_or_minus(array, index + 1, value - array[index])


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!