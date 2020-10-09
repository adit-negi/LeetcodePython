class Solution:
    def divisorGame(self, N: int) -> bool:
        if N>1:
            m = 0
            for i in range(N):
                N-=i
                m+=1
                if N%2==0:
                    return True
                else:
                    return False
