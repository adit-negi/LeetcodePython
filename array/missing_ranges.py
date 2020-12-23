class Solution:

    def findMissingRanges(self, nums, lower, upper):
        res = []
        nums = [lower-1] + nums + [upper+1]
        for i in range(1, len(nums)):
            curr, prev = nums[i], nums[i-1]
            if curr - prev > 1:
                self.addRange(res, prev, curr)
        return res

    def addRange(self, res, low, high):
        if low + 2 == high:
            res.append(str(low+1))
        else:
            res.append(str(low+1) + '->' + str(high-1))
