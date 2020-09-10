#
# @lc app=leetcode.cn id=494 lang=python
#
# [494] 目标和
#

# @lc code=start
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.nums = nums
        self.S = S
        self.total = 0
        self.sum_next(0, 0, '+')
        self.sum_next(0, 0, '-')
        return self.total

    
    def sum_next(self, i, sam, opt):
        if opt == '+':
            sam = sam + self.nums[i]
        else:
            sam = sam - self.nums[i]
        i = i + 1
        if i == len(self.nums):
            if sam == self.S:
                self.total += 1
            return
        self.sum_next(i, sam, '+')
        self.sum_next(i, sam, '-')


class Solution2(object):
    
    def findTargetSumWays(self, nums, S):
        totalSum = sum(nums)
        if(S not in range(-1 * totalSum, totalSum + 1) ): return 0
        dp = [ [ 0 for j in range( totalSum*2 + 1 ) ] for i in range(len(nums))]
        
        ## BASE CASE ## FIRST ROW ##
        dp[0][totalSum + nums[0]] += 1
        dp[0][totalSum - nums[0]] += 1
        
        for i in range(1, len(nums)):
            for j in range( totalSum*2 + 1 ):
                
                if( j - nums[i] >= 0 and dp[i-1][j-nums[i]] > 0 ):          # left side
                    dp[i][j] += dp[i-1][j-nums[i]]
                
                if( j + nums[i] <= totalSum*2 and dp[i-1][j+nums[i]] > 0 ): # right side
                    dp[i][j] += dp[i-1][j+nums[i]]
        
        return dp[-1][totalSum + S]


class Solution3(object):

    def findTargetSumWays(self, nums, S):

        cache = {}

        def dfs(cur, nums):
            key = (cur, tuple(nums))
            if key in cache:
                return cache[key]
            if not nums:
                if cur == S:
                    return 1
                else:
                    return 0
            res = dfs(cur + nums[0], nums[1:]) + dfs(cur - nums[0], nums[1:])
            cache[key] = res
            return res
        
        return dfs(0, nums)



if __name__ == "__main__":
    print(Solution3().findTargetSumWays([1,1,1,1,1], 3))
    
# @lc code=end

