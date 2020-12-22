class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        Q = deque()
        for i in range(n-1, -1, -1):
            if i == n-1:
                dp = nums[i]
            else:
                dp = nums[i]+Q[-1][0]

            while Q and dp >= Q[0][0]:
                Q.popleft()
            Q.appendleft((dp, i))

            while Q and Q[-1][1] > i+k-1:
                Q.pop()
            # print(Q)
        return dp
