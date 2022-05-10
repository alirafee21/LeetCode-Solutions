class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0];
        else:
            tot_sum = 0 
            max_sub = nums[0]
            for i in nums:
                if tot_sum < 0:
                    tot_sum = 0
                tot_sum += i;
                max_sub = max(tot_sum, max_sub)
            return max_sub
            