target = 14
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15, 16]

def is_existing_target_number_sequential(target, number_list):
    for number in number_list:
        if target == number:
            return True

    return False

result = is_existing_target_number_sequential(target, number_list)
print(result)
