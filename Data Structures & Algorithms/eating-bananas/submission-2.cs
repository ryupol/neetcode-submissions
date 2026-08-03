public class Solution {
    public int MinEatingSpeed(int[] piles, int h) {
        int l = 1, r = piles.Max();
        int res = r;
        
        while (l <= r) {
            int m = l + ((r - l) / 2);

            int totalTime = 0;
            foreach (int p in piles) {
                totalTime += (int)Math.Ceiling((double)p / m);
            }

            if (totalTime <= h) {
                res = m;
                r = m - 1;
            }  else {
                l = m + 1;
            }
        }
        return res;
    }
}
