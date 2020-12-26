class Solution:
    def canCompleteCircuit(self, gas, cost):
        def helper(index):
            cnt = 0
            g, c = 0, 0
            while cnt < len(gas):
                g += gas[index]-cost[index]
                if g < 0:
                    return False
                if index < len(gas)-1:
                    index += 1
                else:
                    index = 0
                cnt += 1
            return True
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                if helper(i):
                    return i
        return -1
