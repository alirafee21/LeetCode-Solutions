# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        return self.helper(n,l,r)
        
        
    def helper(self, n, l, r):
        if l >= r:
            if isBadVersion(l):
                return l
            else:
                return 
        mid = (l+r)//2
        if isBadVersion(mid):
            return self.helper(n,l,mid)
        else:
            return self.helper(n,mid+1,r)