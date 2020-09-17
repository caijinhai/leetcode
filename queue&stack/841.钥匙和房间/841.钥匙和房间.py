#
# @lc app=leetcode.cn id=841 lang=python
#
# [841] 钥匙和房间
#
import collections
# @lc code=start
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        queue = collections.deque()
        queue.append(0)
        visited = set([0])
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)
        if len(rooms) == len(visited):
            return True
        return False
    
if __name__ == "__main__":
    print(Solution().canVisitAllRooms([[1,3],[3,2,1],[2],[0]]))
            


        
# @lc code=end

