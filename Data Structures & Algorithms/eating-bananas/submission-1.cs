public class Solution {
    public int MinEatingSpeed(int[] piles, int h) {
        int l = 1, r = piles.Max();

        int res = r;
        while (l <= r) {
            int m = l + ((r - l) / 2);

            int times = 0;
            foreach (int p in piles) {
                times += (p + m - 1) / m;
            }

            if (times <= h) {
                res = Math.Min(res, m);
                r = m - 1;
            }  else {
                l = m + 1;
            }
        }
        return res;
    }
}
