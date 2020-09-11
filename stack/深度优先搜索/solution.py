
class Solution(object):
    '''
    深度优先搜索
    递归嵌套版本
    '''
    def __init__(self):
        pass

    def dfs(self, cur, target, visited):
        if cur == target:
            return True
        for next in cur.neighbors:
            if next in visited:
                visited.append(next)
                if self.dfs(next, target, visited):
                    return True
        return False


import collections
class Solution2(object):
    '''
    深度优先搜索
    显示使用stack版本
    '''
    def dfs(self, root, target):
        stack = collections.deque() 
        visited = {}

        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur == target:
                return True
            for next in cur.neighbors:
                if next not in visited:
                    visited[next] = 1
                    stack.append(next)
        return False