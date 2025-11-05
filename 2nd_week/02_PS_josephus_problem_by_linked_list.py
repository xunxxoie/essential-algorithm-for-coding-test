class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self, data):
        self.size = 1
        self.head = Node(data)
        self.head.next = self.head

    # 마지막에 삽입
    def append(self, data):
        new_node = Node(data)

        # 원소가 하나 밖에 없는 경우
        if self.head.next == self.head:
            self.head.next = new_node
            new_node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next

            cur.next = new_node
            new_node.next = self.head

        self.size += 1

def josephus_problem(n, k):
    # 원형 연결 리스트 정의
    circular_linked_list = CircularLinkedList(1)

    # 원형 연결 리스트 초기화
    if n != 1:
        i = 2
        while i != n+1:
            circular_linked_list.append(i)
            i += 1

    result = "<"

    # 시작점은 헤드 노드
    cur = circular_linked_list.head

    # 원형 연결리스트가 비어있기 전까지
    while circular_linked_list.size != 0:

        if k == 1:
            while cur.next != circular_linked_list.head:
                cur = cur.next
            if circular_linked_list.size == 1:
                result = result + str(cur.next.data)
            else:
                result = result + str(cur.next.data) + ", "
            cur.next = circular_linked_list.head.next
            circular_linked_list.head = cur.next

            cur = cur.next
        elif k == 2:
            if circular_linked_list.size == 1:
                result = result + str(cur.next.data)
            else:
                result = result + str(cur.next.data) + ", "
            cur.next = cur.next.next
            cur = cur.next
        else:
            i = 0
            while i < k-2:
                cur = cur.next
                i+=1

            if circular_linked_list.size == 1:
                result = result + str(cur.next.data)
            else:
                result = result + str(cur.next.data) + ", "

            cur.next = cur.next.next
            cur = cur.next

        circular_linked_list.size -= 1

    return result + ">"


n, k = map(int, input().split())
print(josephus_problem(n, k))