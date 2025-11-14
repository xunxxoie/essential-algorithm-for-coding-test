# 꼭 다시 풀어보기

def get_receiver_top_orders_stack(heights):
    stack = []
    result = [0] * len(heights)

    for i in range(len(heights)):
        # 현재 스택에 들어있는 높이들은 내림차순으로 들어있다 가정

        # 1) 선택된 원소가 스택 마지막의 원소보다 큰 경우
        #   -> 선택된 원소가 앞으로의 레이저를 다 맞음
        #   -> 따라서, 이전 스택에 들어있는 원소들은 필요하지 않음

        # 2) 선택된 원소가 스택 마지막의 원소보다 작은 경우
        #   -> 선택된 원소의 레이저는 스택 마지막의 원소가 맞음
        #   -> 따라서 선택된 원소의 인덱스에 스택 마지막 원소의 인덱스를 기록

        while stack and stack[-1][1] <= heights[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1][0] + 1

        stack.append([i, heights[i]])

    return result

n = input()
heights = list(map(int, input().split()))

print(*get_receiver_top_orders_stack(heights))