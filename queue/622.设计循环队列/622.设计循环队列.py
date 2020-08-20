#
# @lc app=leetcode.cn id=622 lang=python
#
# [622] 设计循环队列
#

# @lc code=start
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.head = -1
        self.tail = -1
        self.size = k
        self.arr = []
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.head == -1:
            self.head = 0
        self.tail += 1
        if self.tail >= self.size :
            self.tail = 0
        if self.tail >= len(self.arr):
            self.arr.append(value)
        else:
            self.arr[self.tail] = value
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head += 1
            if self.head >= self.size:
                self.head = 0
        return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.head]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.tail]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.head == -1 and self.tail == -1:
            return True
        return False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if (self.tail - self.head) == (self.size - 1):
            return True
        if (self.head - self.tail) == 1:
            return True
        return False

        


# Your MyCircularQueue object will be instantiated and called as such:

if __name__ == "__main__":
    obj = MyCircularQueue(3)
    print(obj.enQueue(1))
    print(obj.enQueue(2))
    print(obj.enQueue(3))
    print(obj.enQueue(4))
    print(obj.Rear())
    print(obj.isFull())
    print(obj.deQueue())
    print(obj.enQueue(4))
    print(obj.Rear())

# @lc code=end

