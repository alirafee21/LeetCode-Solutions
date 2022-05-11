class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l, r = 0, len(nums) - 1
        return self.helper(nums, l, r, target)
            
    def helper(self, nums, l, r, target):
        if l >= r:
            if nums[l] == target:
                return l
            else:
                return -1
        else:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return self.helper(nums, l, mid - 1, target)
            else:
                return self.helper(nums, mid + 1, r, target)
            
        