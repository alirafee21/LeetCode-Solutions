import java.util.HashSet;
class Solution {
    
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> dups = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++)
        {
        if (dups.contains(nums[i]))
            {
            return true;   
            }
            dups.add(nums[i]);
        }
        return false;
    }
}
