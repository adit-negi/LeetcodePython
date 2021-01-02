class Solution:
    def peopleIndexes(self, fc: List[List[str]]) -> List[int]:
        m = []
        for i in fc:
            m.append(set(i))

        def checker(arr, a):
            f = False
            for i in arr:
                if i not in a:
                    f = True
            return f
        out = []
        for i in range(len(fc)):
            for j in range(len(m)):
                f = True
                if j == i:
                    continue
                if not checker(fc[i], m[j]):
                    f = False
                    break
            if f:
                out.append(i)
        return out
