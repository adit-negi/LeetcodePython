class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetset = {}

        def GetKey(val):
            for key, value in targetset.items():
                if val == value:
                    return key

        for i in range(len(nums)):

            if nums[i] in targetset.values():

                return [i, GetKey(nums[i])]
                break
            targetset[i] = (target-nums[i])
