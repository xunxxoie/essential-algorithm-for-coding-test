import math

input = 20

def find_prime_list_under_number(number):
    prime_list = []
    for num in range(2, number + 1):
        for i in prime_list:
            if i <= math.sqrt(num) and num % i == 0:
                break
        else:
            prime_list.append(num)

    return prime_list

result = find_prime_list_under_number(input)
print(result)

# 소수 찾기에서의 개선점
# 1) 이전에 찾은 소수로 나누어떨어지는가? 만으로도 소수 판별이 가능하다.
# 2) 타겟 넘버 n의 제곱근 이하의 수로만 판별해도 충분하다.