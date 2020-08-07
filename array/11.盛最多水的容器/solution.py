
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        count = len(height)
        left = 0
        right = count - 1
        max_area = 0
        for index in range(0, count):
            val = min([height[left], height[right]])
            area = val * abs(right - left)
            print(left, right, area)
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    print(Solution().maxArea([1,3,2,5,25,24,5]))
