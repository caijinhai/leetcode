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


class Template(object):
    '''
    广度优先搜索模版
    先遍历完上一层再遍历下一层
    '''
    def __init__(self):
        pass

    def bfs(self, root, target):
        queue = Queue()

        queue.put(root)

        while queue:
            size = queue.__sizeof__
            for i in range(size):
                cur = queue.get()
                if cur == target:
                    return True
                for neighbor in cur.neighbors:
                    queue.put(neighbor)
        return False
