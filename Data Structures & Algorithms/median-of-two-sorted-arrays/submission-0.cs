public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] A = nums1, B = nums2;
        int total = A.Length + B.Length;
        int half = total / 2;

        if (A.Length > B.Length) 
            (A, B) = (B, A);
        
        int l = 0, r = A.Length - 1;

        while (true) {
            int m = (int)Math.Floor((double)(l + r) / 2);
            int x = half - m - 2;

            int leftA = (m >= 0) ? A[m] : int.MinValue;
            int leftB = (x >= 0) ? B[x] : int.MinValue;
            int rightA = (m + 1 < A.Length) ? A[m + 1] : int.MaxValue;
            int rightB = (x + 1 < B.Length) ? B[x + 1] : int.MaxValue;

            if (leftA <= rightB && leftB <= rightA) {
                int rightMin = Math.Min(rightA, rightB);
                int leftMax = Math.Max(leftA, leftB);
                if (total % 2 == 0) {
                    return (rightMin + leftMax) / 2.0;
                }
                return rightMin;
            }
            else if (leftA > rightB) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
    }
}
