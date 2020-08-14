
class Solution(object):

    def buildNext(self, s, i):
        cur = s[0:i]
        print(cur)
        arr = []
        number = 0
        for index in range(1, len(cur)):
            if cur[0:index] in arr:
                number = len(cur[0:index])
            arr.append(cur[0:index])
            if cur[0:index][::-1] in arr:
                number = len(cur[0:index])
            arr.append(cur[0:index][::-1])
        return number
        

    def kmp(self, s):
        p = []
        p[0] = -1
        for i in range(1, len(s)):
            p[i] = self.buildNext(s, i)
        print(p)

if __name__ == "__main__":
    print(Solution().kmp('abcda'))

