class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0
        j = n - 1
        while i <= j:
            a = s[j]
            s[j] = s[i]
            s[i] = a
            i += 1
            j -= 1
        return s

if __name__ == "__main__":
    print(Solution().reverseString(["h","e","l","l","o","w"]))

