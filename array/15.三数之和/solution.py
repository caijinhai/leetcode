class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        if n < 3:
            return []
        res = []
        for first in range(0, n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = n - 1
            target = 0 - nums[first]
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and (nums[second] + nums[third]) > target:
                    third -= 1
                if second == third:
                    break
                if (nums[second] + nums[third]) == target:
                        res.append([nums[first], nums[second], nums[third]])
                
        return res

if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,2,-1,-4]))
            

