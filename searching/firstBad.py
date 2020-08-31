# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high =  n
        if n==1:
            if isBadVersion(1) == True:
                return 1
            else:
                return False
        while low<=high:
            mid = (low+high)//2
            if isBadVersion(mid-1) == 0 and isBadVersion(mid)==1 :
                return mid
            elif isBadVersion(mid-1)==1 and isBadVersion(mid) == True:
                high = mid
            elif isBadVersion(mid-1) == 0 and isBadVersion(mid)==False:
                low = mid+1
        return False
                
