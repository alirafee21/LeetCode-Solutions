class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 1
        dic = {}
        max_eval = 0
        for i, charac in enumerate (s):
            if charac in dic and dic[charac] >= left:
                left = dic[charac] + 1 
            dic[charac] = i
            max_eval = max(max_eval, right - left)
            right += 1
        return max_eval