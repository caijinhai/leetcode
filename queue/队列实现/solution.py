
class MyQueue(object):

    def __init__(self):
        self.p_start = 0
        self.queues = []

    def enqueue(self, x):
        self.queues.append(x)
    
    def dequeue(self):
        if self.is_empty():
            return False
        self.p_start = self.p_start + 1
        return True

    def get(self):
        return self.queues[self.p_start]

    def is_empty(self):
        if self.p_start >= len(self.queues):
            return True
        return False


if __name__ == "__main__":
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.get())
    queue.dequeue()
    print(queue.get())
    print(queue.is_empty())

