


class Solution:
    '''
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [0, 0]
        for index, num in enumerate(nums):
            find_index = self.find_value(nums[index + 1:], target - num, index)
            if find_index != -1:
                res = [index, find_index]
                break
        return res

    def find_value(self, arr, val, p):
        find_index = -1
        for index, item in enumerate(arr):
            if item == val:
                find_index = p + 1 + index
                break
        return find_index


