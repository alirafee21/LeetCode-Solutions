class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        save = {'}' : '{', ')' : '(', ']' : '[' }
        for brac in s:
            if brac in "([{":
                lst.append(brac)
            elif brac in ")]}":
                if (len(lst) > 0) :
                    b = lst.pop()
                    if save[brac] != b:
                        return False
                else:
                    return False
        if len(lst) > 0:
            return False
        return True