class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(maxsize=None)
        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            to_return = 0
            start = max(0, target-f)
            for k in range(start, target):
                to_return += dp(d-1, k)
            return to_return
        return dp(d, target) % (10**9 + 7)
