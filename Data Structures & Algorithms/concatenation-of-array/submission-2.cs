public class Solution {
    public int[] GetConcatenation(int[] nums) {
        var ans = nums.Concat(nums);

        return ans.ToArray();
    }
}