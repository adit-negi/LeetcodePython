class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = float('-inf')
        cur = 0
        # sliding window; current value = [i, j]
        seen = set()
        i = 0
        for j in range(len(nums)):
            while nums[j] in seen:
                cur -= nums[i]
                seen.remove(nums[i])
                i += 1
            seen.add(nums[j])
            cur += nums[j]
            ans = max(ans, cur)

        return ans
