class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_el = nums[0]
        count = 0
        
        for i in nums:
            if i != maj_el:
                count -= 1
                if count == 0:                    
                    count += 1
                    maj_el = i
            else:
                count += 1
        return maj_el
                