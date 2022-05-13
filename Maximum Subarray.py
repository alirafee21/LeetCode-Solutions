class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        curr = nums[0]
        for num in nums: 
            if temp < 0:
                temp = 0
            temp = temp + num
            curr = max(temp, curr)
        return curr 
