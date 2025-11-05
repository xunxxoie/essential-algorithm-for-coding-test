def count_down(number):
    print(number)
    if number == 0:
        return
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)

# 재귀함수는 종료조건이 중요하다!