class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        left_arr = []
        left_sum = 0
        for index in range(0, count):
            left_sum += nums[index]
            left_arr.append(left_sum)
        
        right_arr = []
        right_sum = 0
        for index in range(count, 0, -1):
            right_sum += nums[index - 1]
            right_arr.append(right_sum)

        find_index = -1
        for index, val in enumerate(left_arr):
            if val == right_arr[count - 1 - index]:
                find_index = index
                break
        return find_index

if __name__ == '__main__':
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))

