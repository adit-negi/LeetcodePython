class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}
        for i in range(len(nums1)):
            if nums1[i] in dict1:
                dict1[nums1[i]] = dict1[nums1[i]]+1
            else:
                dict1[nums1[i]] = 1

        for i in range(len(nums2)):
            if nums2[i] in dict2:
                dict2[nums2[i]] = dict2[nums2[i]]+1
            else:
                dict2[nums2[i]] = 1
        outputList = []
        for key in dict1:
            if key in dict2:
                number_of_intersections = min(dict1[key], dict2[key])
                tempList = [key]*number_of_intersections
                outputList.extend(tempList)
        return outputList
