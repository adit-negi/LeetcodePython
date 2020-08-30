class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        largest = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < largest:
                largest = len(strs[i])
        longest_prefix = ""
        flag = 0
        if len(strs) == 1:
            return strs[0]
        for j in range(largest):
            for i in range(len(strs)-1):

                if strs[i][j] == strs[i+1][j]:
                    flag = 1

                else:
                    flag = 0
                    break
            if flag == 0:
                break
            if flag == 1:
                longest_prefix = longest_prefix + strs[0][j]

        return longest_prefix
