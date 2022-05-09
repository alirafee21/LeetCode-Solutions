class Solution {
    public int[] twoSum(int[] nums, int target) {
        int intArray[];
        intArray = new int[2];
        for (int i = 0; i < nums.length; i++)
        {
            int g = i + 1;
            while (g < nums.length) 
            {
                if (nums[i] + nums[g] == target)
                {
                    intArray[0] = i;
                    intArray[1] = g;
                    return intArray;
                }
                g ++;
                
            }
        }
        return intArray;
    }
}