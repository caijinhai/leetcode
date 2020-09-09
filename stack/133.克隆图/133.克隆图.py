#
# @lc app=leetcode.cn id=133 lang=python
#
# [133] 克隆图
#

# @lc code=start

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    '''
    深度优先搜索解决方式
    '''
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(item) for item in node.neighbors]
    
        return clone_node


from collections import deque
class Solution2(object):
    '''
    广度优先搜索解决方式
    '''
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node):
        if not node:
            return node
        queue = deque()
        queue.append(node)
        self.visited[node] = Node(node.val, [])

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in self.visited:
                    clone_neighbor = Node(neighbor.val, [])
                    self.visited[neighbor] = clone_neighbor
                    queue.append(neighbor)
 
                self.visited[cur].neighbors.append(self.visited[neighbor])
        return self.visited[node]


# @lc code=end

