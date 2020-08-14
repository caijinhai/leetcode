
class Solution(object):

    def buildNext(self, s):
        m = len(s)
        j = 0
        p = []
        p.append(-1)
        t = -1
        while (j < (m - 1)):
            if (0 > t or s[j] == s[t]):
                j += 1
                t += 1
                p.append(t)
            else:
                t = p[t]
        return p
    
    def match(self, find_s, all_s):
        next = self.buildNext(find_s)
        m = len(all_s) # 文本串
        i = 0
        n = len(find_s) # 模式串
        j = 0

        while (i < m and j < n):
            if (0 > j or find_s[j] == all_s[i]):
                i += 1
                j += 1
            else:
                j = next[j]
        next = []
        return i - j



if __name__ == "__main__":
    print(Solution().match('ACTGPACY', 'ACTGPACTGKACTGPACY'))

