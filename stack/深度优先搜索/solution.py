
class Solution(object):

    def __init__(self):
        pass

    def dfs(self, cur, target, visited):
        if cur == target:
            return True
        for next in cur.neighbors:
            if next not in visited:
                visited.append(next)
                if self.dfs(next, target, visited):
                    return True
        return False
