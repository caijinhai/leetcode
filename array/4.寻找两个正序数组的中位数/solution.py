class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 == 0:
            if len2 % 2 == 0:
                return (nums2[int(len2 / 2 - 1)] + nums2[int(len2 / 2)]) / 2
            else:
                return nums2[int(len2 / 2)]

        if len2 == 0:
            if len1 % 2 == 0:
                return (nums1[int(len1 / 2 - 1)] + nums1[int(len1 / 2)]) / 2
            else:
                return nums1[int(len1 / 2)]

        merge_nums = []
        first = 0
        second = 0
        while first < len1 and second < len2:
            if nums1[first] < nums2[second]:
                merge_nums.append(nums1[first])
                first += 1
            else:
                merge_nums.append(nums2[second])
                second += 1

        if first < len1:
           for index in range(first, len1):
                merge_nums.append(nums1[index]) 

        if second < len2:
            for index in range(second, len2):
                merge_nums.append(nums2[index])
    
        total_len = len1 + len2
        if total_len % 2 == 0:
            return (merge_nums[int(total_len / 2 - 1)] + merge_nums[int(total_len / 2)]) / 2
        else:
            return merge_nums[int(total_len / 2)]


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([4, 5, 6, 8, 9], []))
