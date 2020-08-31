class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k,i,j = 0,0,0
        while i< len(nums1) and j < len(nums2):
            if nums1[i]> nums2[j]:
                temp = nums1[i]
                nums1[i] = nums2[j]
                j+=1
                nums1.pop()
                nums1.insert(i+1,temp)
            else:
                i+=1
        lenght_left = len(nums1) - (len(nums2)-j)
        while j< len(nums2):
            nums1[lenght_left] = nums2[j]
            j+=1
            lenght_left+=1
         
