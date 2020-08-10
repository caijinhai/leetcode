

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda item: item[0])

        if len(intervals) < 1:
            return intervals
        
        i = 0
        res = [intervals[0]]
        while i < (len(intervals) - 1):
            items = self.__do_merget(res[-1], intervals[i+1])
            res = res[0: -1]
            for item in items:
                res.append(item)
            i += 1
        return res
        

    def __do_merget(self, left, right):
        start, end = left
        start2, end2 = right
        if start2 <= end:
            arr = [[start, end2]]
            if end2 <= end:
                arr = [[start, end]]
        else:
            arr = [[start, end], [start2, end2]]
        return arr


class Solution2(object):
    def merge(self, intervals):
        intervals.sort(key=lambda item: item[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

if __name__ == "__main__":
    print(Solution2().merge([[1,3],[2,6],[8,10],[15,18]]))
