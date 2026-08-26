class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)

        def dfs(remaining):
            if remaining == 0:
                return 0

            if remaining in memo:
                return memo[remaining]

            res = 10001
            for coin in coins:
                if remaining - coin >= 0:
                    res = min(res, 1 + dfs(remaining - coin))
            memo[remaining] = res
            return res
            
        minCoins = dfs(amount)
        return minCoins if minCoins != 10001 else -1
         

