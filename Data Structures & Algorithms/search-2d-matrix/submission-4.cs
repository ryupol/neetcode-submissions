public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int m = matrix.Length, n = matrix[0].Length;
        
        // Find row target
        int t = 0, b = m - 1;
        int row = 0;
        while (t <= b) {
            row = t + ((b - t) / 2);

            if (matrix[row][n - 1] < target) {
                t = row + 1;
            } else if (matrix[row][0] > target){
                b = row - 1;
            } else break;
        }
        if (t > b) return false;
        // Find target
        int l = 0, r = n - 1;
        while (l <= r) {
            int mid = l + ((r - l) / 2);

            if (matrix[row][mid] < target) {
                l = mid + 1;
            } else if (matrix[row][mid] > target) {
                r = mid - 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
