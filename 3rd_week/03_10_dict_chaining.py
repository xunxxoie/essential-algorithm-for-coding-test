class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self,key):
        for k, v in self.items:
            if k is key:
                return v

class LinkedDict:
    def __init__(self, length):
        self.items = []
        self.length = length
        for i in range(length):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % self.length
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % self.length
        return self.items[index].get(key)