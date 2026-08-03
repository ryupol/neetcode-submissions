public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int m = matrix.Length, n = matrix[0].Length;
        int left = 0, right = (m * n) - 1;

        while (left <= right) {
            int mid = left + ((right - left) / 2);

            int row = mid / n;
            int col = mid % n;

            if (matrix[row][col] < target) {
                left = mid + 1;
            } else if (matrix[row][col] > target) {
                right = mid - 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
