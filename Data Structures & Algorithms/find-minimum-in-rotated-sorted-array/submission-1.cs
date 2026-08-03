public class Solution {
    public int FindMin(int[] nums) {
        // [3 5 2]
        // shift_l => m lowest, l lowest
        // shift_r => r lowest

        int l = 0, r = nums.Length - 1;
        int res = nums[0];
        while (l <= r) {
            int m = (r + l) / 2;

            res = Math.Min(res, nums[m]);

            if ((nums[l] < nums[m] && nums[l] < nums[r]) || (nums[m] < nums[l] && nums[m] < nums[r])) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return res;
    }
}
