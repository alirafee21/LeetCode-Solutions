class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for char in magazine:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] = dict[char] + 1
        for char in ransomNote:
            if char not in dict:
                return False
            else:
                dict[char] = dict[char] - 1
                if dict[char] == 0:
                    del dict[char]
        return True