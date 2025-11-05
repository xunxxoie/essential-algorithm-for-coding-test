shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "순대"]


def is_available_to_order(menus, orders):
    shop_menus.sort()

    for order in orders:
        if not is_exist_target_menu_binary(order, menus):
            return False

    return True

def is_exist_target_menu_binary(target, array):
    start_index = 0
    end_index = len(array)
    mid_index = (start_index + end_index) // 2

    while start_index <= end_index:
        if array[mid_index] == target:
            return True
        elif array[mid_index] > target:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

        mid_index = (start_index + end_index) // 2

    return False



result = is_available_to_order(shop_menus, shop_orders)
print(result)