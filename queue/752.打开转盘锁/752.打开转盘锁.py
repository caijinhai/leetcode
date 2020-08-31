#
# @lc app=leetcode.cn id=752 lang=python
#
# [752] 打开转盘锁
#
import collections
# @lc code=start
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends_set = set(deadends)
        my_queue = collections.deque()
        visited = set()

        my_queue.append(('0000', 0))

        while my_queue:
            string, step = my_queue.popleft()
            if string in deadends_set:
                continue
            if string == target:
                return step

            for i in range(len(string)):
                for num in (-1,1):
                    re_num = (int(string[i]) + num) % 10
                    re_string = string[:i] + str(re_num) + string[i+1:]
                    if re_string not in visited:
                        visited.add(re_string)
                        my_queue.append((re_string, step + 1))
        return -1

if __name__ == "__main__":
    print(Solution().openLock(["8888"], "0009"))

# @lc code=end

