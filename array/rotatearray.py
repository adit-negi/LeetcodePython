class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1 = nums[(len(nums)-k):len(nums)]
        l2 = nums[:len(nums)-k]

        l1.extend(l2)
        for i in range(len(nums)):
            nums[i] = l1[i]
