class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tot_len = len(s)
        count = 0
        lst = []
        for n in s:
            lst.append(n)

        for n in t:
            if n in lst:
                count += 1
                lst.remove(n)

        if count == tot_len and count == len(t):
            return True
        return False
    


        