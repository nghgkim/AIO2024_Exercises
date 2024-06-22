class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = list()

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        return self.__queue.pop()

    def enqueue(self, value):
        self.__queue.insert(0, value)

    def front(self):
        return self.__queue[-1]


queue1 = MyQueue(capacity=5)

queue1.enqueue(1)

queue1.enqueue(2)

print(queue1.is_full())

print(queue1.front())

print(queue1.dequeue())

print(queue1.front())

print(queue1.dequeue())

print(queue1.is_empty())