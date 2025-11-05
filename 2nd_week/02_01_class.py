# 배열(Array)는 인덱스로 특정 인덱스의 원소에 O(1) 시간복잡도로 조회할 수 있다.
# 따라서, 조회가 잦은 경우 배열이 리스트보다 유리하다.

# 리스트(List)는 O(1)의 시간 복잡도로 특정 원소를 삽입/삭제할 수 있다.
# 따라서, 삽입/삭제가 잦은 경우 리스트가 배열보다 유리하다.

# 파이썬에서는 배열과 리스트의 중간 구현인 동적 배열을 사용한다.
# 따라서, 크기가 고정이 아니며, 원소 삽입/삭제 시 자동으로 리사이징된다.

class Person:
    def __init__(self, name_param): # self는 객체 자신을 의미
        self.name = name_param
        print("hi i am created", self, self.name)

    def talk(self):
        print("안녕하세요 저는 ", self.name, "입니다.")

person_1 = Person("유재석")
person_1.talk()

person_2 = Person("박명수")
person_2.talk()