class Solution:
    def longestPalindrome(self, s):
        result, freq = 0, sorted([s.count(i) for i in set(s)])
        for i in freq:
            if i%2==0:
                result += i
            else:
                if result%2==0:
                    result += 1
                result += i-1
        return result