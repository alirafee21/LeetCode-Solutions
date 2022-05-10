class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = False
        other = True
        str1 = ""
        str2 = ""
        for i in s:
            if i.isalnum():
                str1 = str1+i
        for f in range(len(s)-1,-1, -1):
            if s[f].isalnum():
                str2 = str2 + s[f]
   
        if str1.lower() == str2.lower():
            return True
        return False
        