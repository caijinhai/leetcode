
class Solution(object):

    def __init__(self, count):
        self.p = -1
        self.count = count
        self.stack = [0 for i in range(count)]

    def push(self, val):
        if self.full():
            return False
        self.p = self.p + 1
        self.stack[self.p] = val
        return True

    def pop(self):
        if self.empty():
            return False
        self.p = self.p - 1
        return True

    def top(self):
        if self.empty():
            return -1
        else:
            return self.stack[self.p]

    def empty(self):
        if self.p == -1:
            return True
        return False
    
    def full(self):
        if self.p == (self.count - 1):
            return True
        return False


if __name__ == "__main__":
    stack = Solution(5)
    print(stack.empty())
    print(stack.push(1))
    print(stack.empty())
    print(stack.pop())
    print(stack.empty())
    print(stack.push(1))
    print(stack.push(2))
    print(stack.push(3))
    print(stack.push(4))
    print(stack.push(5))
    print(stack.push(6))
    print(stack.top())
    print(stack.pop())
    print(stack.top())