#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast +=1
            elif nums[fast] > nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
            else:
                break
        return slow + 1
    
if __name__ == "__main__":
    print(Solution().removeDuplicates([1,1,2]))
                
# @lc code=end

