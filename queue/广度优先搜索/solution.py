from queue import Queue


class Solution(object):
    def __init__(self):
        self.queue = Queue()

    def bfs(self, root, target):
        step = 0
        self.queue.put(root)

        while not self.queue.empty():
            step += 1
            cur = self.queue.get()
            if cur.val == target:
                return step
            else:
                if cur.left:
                    self.queue.put(cur.left)
                if cur.right:
                    self.queue.put(cur.right)
        return -1


