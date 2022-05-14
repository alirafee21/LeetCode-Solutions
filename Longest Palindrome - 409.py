class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        di = {}
        for char in s:
            if char not in di:
                di[char] = 1
            else:
                di[char] += 1
        count = 0
        odd_count = 0
        cache = None
        for m in di:
            if di[m] % 2 == 0:
                count += di[m]
            else:
                if cache is None:
                    cache = m
                    odd_count += di[m]
                elif di[m] > odd_count:
                    odd_count -= 1
                    odd_count += di[m]
                else: 
                    odd_count += (di[m] - 1)

        count = count + odd_count
        return count 
                 