#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#
import collections
# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        my_queue = collections.deque()

        my_queue.append((n, 0))
        while my_queue:
            cur, step = my_queue.popleft()
            max = int(pow(cur, 0.5))
            nums = [i*i for i in range(max+1)]
            if cur in nums:
                return step + 1
            if cur < 0:
                continue

            for i in range(max, 0, -1):
                my_queue.append((cur - pow(i, 2), step + 1))
        return 0
        

if __name__ == "__main__":
    print(Solution().numSquares(13))


# @lc code=end

