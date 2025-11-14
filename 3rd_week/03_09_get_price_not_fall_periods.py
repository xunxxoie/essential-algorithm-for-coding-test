from collections import deque

prices = [1, 2, 3, 2, 3]

def get_price_not_fall_periods(prices):
    result = []
    prices_queue = deque(prices)

    while len(prices_queue) != 0:
        now_price = prices_queue.popleft()

        i = 0
        while i < len(prices_queue): # while prices_queue: -> 큐가 비어있지 않을 동안 반복한다는 의미!
            next_price = prices_queue[i]

            if next_price < now_price:
                i += 1
                break

            i += 1

        result.append(i)

    return result


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))