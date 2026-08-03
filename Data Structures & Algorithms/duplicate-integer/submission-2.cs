public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> visited = new HashSet<int>();

        foreach (int num in nums) {
            if (visited.Contains(num)) {
                return true;
            } else {
                visited.Add(num);
            }
        }
        return false;
    }
}
